#!/usr/bin/env python3
"""Regenerate homepage responsive images and their Liquid manifest (requires Pillow).

Run after changing showcase artwork, editor screenshots or platform logos:
    python3 scripts/frontpage_images.py
Original assets remain available for larger displays and other pages.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def game_sources(games):
    return {f"/images/games/{game['images']['third']}": (256, 384, 512)
            for game in games if game.get('showcase') == 'full' and game.get('images', {}).get('third')}


def generate_images(sources, root):
    from PIL import Image

    manifest = {}
    for url, widths in sorted(sources.items()):
        source = root / url.lstrip('/')
        image = Image.open(source).convert('RGBA')
        candidates = []
        for width in widths:
            if width >= image.width:
                continue
            target = source.with_name(f'{source.stem}-{width}w.webp')
            resized = image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
            resized.save(target, 'WEBP', quality=82, method=6)
            candidates.append(f'/{target.relative_to(root).as_posix()} {width}w')
        # Keep an original-resolution WebP candidate, including for PNG logos.
        full = source.with_suffix('.webp')
        if full != source:
            image.save(full, 'WEBP', quality=85, method=6)
        candidates.append(f'/{full.relative_to(root).as_posix()} {image.width}w')
        manifest[url] = ', '.join(candidates)
    return manifest


def write_manifest(root, manifest):
    target = root / '_data/responsive_images.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')


def regenerate_game_images(games, root=Path('.')):
    """Rebuild variants after the showcase importer has pruned obsolete assets.

    Replace all game entries, including deleted/unfeatured games, and preserve
    the independently generated editor and platform image entries.
    """
    root = Path(root)
    target = root / '_data/responsive_images.json'
    previous = json.loads(target.read_text()) if target.is_file() else {}
    manifest = {url: srcset for url, srcset in previous.items()
                if not url.startswith('/images/games/')}
    manifest.update(generate_images(game_sources(games), root))
    write_manifest(root, manifest)


def main():
    games = json.loads((ROOT / '_data/games.json').read_text())
    sources = game_sources(games)
    sources['/images/editor/nosetup-editor.webp'] = (350, 520, 700)
    platform_urls = set(re.findall(r'src="(/images/logo/platform/100px-[^"]+\.png)"',
                                   (ROOT / '_includes/platforms.html').read_text()))
    sources.update({url: (42, 84) for url in platform_urls})
    manifest = generate_images(sources, ROOT)
    write_manifest(ROOT, manifest)
    print(f'Generated responsive variants for {len(manifest)} images.')


if __name__ == '__main__':
    main()
