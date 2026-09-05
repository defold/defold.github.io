#!/usr/bin/env python3
"""Copy example documentation media and prune old loose images using a site build.

Game archives and nested bundle resources are never pruned. Run a fresh Jekyll
build before using this script to clean previously imported example images.
"""
from __future__ import annotations

import argparse
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".webm", ".mp4", ".svg"}
SITE_HOSTS = {"defold.com", "www.defold.com"}


class MediaReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if not value:
                continue
            if name in {"src", "href", "poster", "content", "data-src"}:
                self.urls.add(value)
            elif name == "srcset":
                self.urls.update(part.strip().split()[0] for part in value.split(",") if part.strip())


def local_media_url(url: str, base: str) -> str | None:
    parsed = urlsplit(urljoin("https://www.defold.com" + base, unescape(url)))
    if parsed.hostname not in SITE_HOSTS:
        return None
    path = unquote(parsed.path)
    return path if Path(path).suffix.lower() in MEDIA_SUFFIXES else None


def copy_documentation_images(source: Path, destination: Path, document: str) -> None:
    import markdown
    import yaml

    source, destination = Path(source), Path(destination)
    _, frontmatter, body = document.split("---", 2)
    metadata = yaml.safe_load(frontmatter)
    references = MediaReferences()
    references.feed(markdown.markdown(body, extensions=["fenced_code", "tables"]))
    for key in ("thumbnail", "opengraph_image", "twitter_image"):
        if metadata.get(key):
            references.urls.add(metadata[key])
    # Media embedded through Liquid includes is not an HTML element yet.
    for include in re.findall(r"{%\s*include\b.*?%}", body, re.DOTALL):
        references.urls.update(re.findall(r'''(?:filename|src|image|poster)=["']([^"']+)["']''', include))

    prefix = "/examples/" + metadata["path"].strip("/") + "/"
    for url in sorted(references.urls):
        path = local_media_url(url, prefix)
        if not path or not path.startswith(prefix):
            continue
        relative = Path(path.removeprefix(prefix))
        original = source / relative
        if not original.resolve().is_relative_to(source.resolve()):
            raise RuntimeError(f"Example image is outside its project: {url}")
        if not original.is_file():
            # Existing upstream pages can contain broken image links. Report
            # them without preventing the remaining examples from importing.
            print(f"WARNING: Missing example documentation image: {original}")
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if original.resolve() != target.resolve():
            shutil.copy2(original, target)


def prune_unused_images(site: Path, root: Path = ROOT) -> tuple[int, int]:
    site, root = Path(site), Path(root)
    pages = list((root / "examples").glob("*/*/index.md"))
    if not pages:
        raise RuntimeError("No example pages found; refusing to prune images")
    for page in pages:
        built_page = site / page.relative_to(root).with_suffix(".html")
        if not built_page.is_file() or built_page.stat().st_mtime < page.stat().st_mtime:
            raise RuntimeError(f"A fresh Jekyll build is required: {built_page}")

    candidates = {
        "/" + path.relative_to(root).as_posix(): path
        for page in pages
        for path in page.parent.iterdir()
        if path.is_file() and path.suffix.lower() in MEDIA_SUFFIXES
    }
    used = set()
    token_pattern = re.compile(r'''[^\s"'<>()[\]{}]+''')
    for path in site.rglob("*"):
        if not path.is_file() or path.suffix not in {".html", ".js", ".css", ".json", ".xml", ".txt", ".md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        references = MediaReferences()
        if path.suffix == ".html":
            references.feed(text)
        # Keep literal media URLs in scripts, styles, metadata and code samples too.
        urls = references.urls | {
            token for token in token_pattern.findall(text)
            if any(suffix in token.lower() for suffix in MEDIA_SUFFIXES)
        }
        base = "/" + path.relative_to(site).as_posix()
        for url in urls:
            local = local_media_url(url, base)
            if local in candidates:
                used.add(local)

    if not used:
        raise RuntimeError("No example image references found; refusing to prune images")
    unused = candidates.keys() - used
    removed_bytes = sum(candidates[url].stat().st_size for url in unused)
    for url in sorted(unused):
        candidates[url].unlink()
    return len(unused), removed_bytes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True, help="Fresh Jekyll output directory")
    args = parser.parse_args()
    count, size = prune_unused_images(args.site)
    print(f"Removed {count} unused loose example images ({size / (1 << 20):.2f} MiB)")
