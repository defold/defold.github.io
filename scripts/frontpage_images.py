#!/usr/bin/env python3
"""Regenerate homepage responsive images and their Liquid manifest (requires Pillow).

Run after changing showcase artwork, editor screenshots or platform logos:
    python3 scripts/frontpage_images.py
Original assets remain available for larger displays and other pages.
"""
import json
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def main():
    games = json.loads((ROOT / '_data/games.json').read_text())
    sources = {f"/images/games/{game['images']['third']}": (256, 384, 512)
               for game in games if game.get('showcase') == 'full' and game.get('images', {}).get('third')}
    sources['/images/editor/nosetup-editor.webp'] = (350, 520, 700)
    platform_urls = set(re.findall(r'src="(/images/logo/platform/100px-[^"]+\.png)"',
                                   (ROOT / '_includes/platforms.html').read_text()))
    sources.update({url: (42, 84) for url in platform_urls})
    manifest = {}
    for url, widths in sorted(sources.items()):
        source = ROOT / url.lstrip('/')
        image = Image.open(source).convert('RGBA')
        candidates = []
        for width in widths:
            if width >= image.width:
                continue
            target = source.with_name(f'{source.stem}-{width}w.webp')
            resized = image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
            resized.save(target, 'WEBP', quality=82, method=6)
            candidates.append(f'/{target.relative_to(ROOT).as_posix()} {width}w')
        # Keep an original-resolution WebP candidate, including for PNG logos.
        full = source.with_suffix('.webp')
        if full != source:
            image.save(full, 'WEBP', quality=85, method=6)
        candidates.append(f'/{full.relative_to(ROOT).as_posix()} {image.width}w')
        manifest[url] = ', '.join(candidates)
    (ROOT / '_data/responsive_images.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Generated responsive variants for {len(manifest)} images.')


if __name__ == '__main__':
    main()
