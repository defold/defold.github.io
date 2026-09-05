import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import dedupe_examples_wasm as wasm
from scripts.example_images import copy_documentation_images, prune_unused_images


def loader_fixture():
    lines = ["var EngineLoader = {"]
    for artifact in wasm.ARTIFACTS:
        filename = ("1" if artifact.suffix == ".wasm" else "2") * 32 + artifact.suffix
        lines.append(f"    {artifact.size_property}: 0,")
        lines.append(f'    {artifact.property_name}: "/examples/wasm/{filename}",')
    lines.extend([
        "};",
        'Module["locateFile"] = function(path, scriptDirectory)',
        "{",
        "    return scriptDirectory + path;",
        "};",
    ])
    return "\n".join(lines)


class WasmCacheTests(unittest.TestCase):
    def test_existing_loaders_survive_repeated_runs_and_stale_cache_is_removed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            examples = root / "examples"
            cache = examples / "wasm"
            cache.mkdir(parents=True)
            loader = examples / "basics" / "fixture" / "dmloader.js"
            loader.parent.mkdir(parents=True)
            fixture = loader_fixture()
            loader.write_text(fixture)
            for filename in {"1" * 32 + ".wasm", "2" * 32 + ".wasm.js"}:
                (cache / filename).write_bytes(b"active fixture")
            stale = cache / ("0" * 32 + ".wasm")
            stale.write_bytes(b"stale")
            with patch.multiple(wasm, ROOT=root, EXAMPLES_DIR=examples, DEDUP_DIR=cache), contextlib.redirect_stdout(io.StringIO()):
                self.assertTrue(wasm.run())
                first = loader.read_text()
                self.assertFalse(wasm.run())
            self.assertEqual(first, loader.read_text())
            self.assertIn('wasm_file: "/examples/wasm/' + "1" * 32 + '.wasm"', first)
            self.assertIn("wasm_pthread_size: 14,", first)
            self.assertFalse(stale.exists())

    def test_fresh_unthreaded_bundle_gets_shared_urls_and_thread_fallbacks(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cache = root / "examples/wasm"
            loader = root / "examples/basics/fixture/dmloader.js"
            loader.parent.mkdir(parents=True)
            fixture = loader_fixture()
            for artifact in wasm.ARTIFACTS:
                fixture = "\n".join(line for line in fixture.splitlines() if not line.strip().startswith(artifact.property_name + ":"))
                if "_pthread" not in artifact.property_name:
                    (loader.parent / artifact.filename).write_bytes(b"shared wasm" if artifact.suffix == ".wasm" else b"shared js")
            loader.write_text(fixture)
            with patch.multiple(wasm, ROOT=root, EXAMPLES_DIR=root / "examples", DEDUP_DIR=cache), contextlib.redirect_stdout(io.StringIO()):
                wasm.run()
                self.assertFalse(wasm.run())
            self.assertEqual(len(list(cache.iterdir())), 2)
            self.assertTrue(all(not (loader.parent / a.filename).exists() for a in wasm.ARTIFACTS))

    def test_missing_live_artifact_prevents_cache_pruning(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            loader = root / "dmloader.js"
            loader.write_text('wasm_file: "/examples/wasm/' + "1" * 32 + '.wasm",')
            stale = root / ("0" * 32 + ".wasm")
            stale.write_bytes(b"stale")
            with patch.object(wasm, "DEDUP_DIR", root), self.assertRaisesRegex(RuntimeError, "Missing cached artifact"):
                wasm.prune_unused_artifacts([loader])
            self.assertTrue(stale.exists())


class ExampleImageTests(unittest.TestCase):
    def test_import_copies_documented_media_preserving_paths_and_ignores_project_textures(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, destination = root / "source", root / "output"
            source.mkdir()
            for filename in ("thumbnail.webp", "images/setup image.png", "movie.mp4", "game/texture.png", ".internal/dependency/header.png"):
                path = source / filename
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"image")
            document = '''---
path: basics/fixture
thumbnail: thumbnail.webp
---
![Setup](images/setup%20image.png)
<video src="movie.mp4"></video>
![External](https://example.com/external.png)
![Shared](/images/shared.png)
'''
            copy_documentation_images(source, destination, document)
            self.assertEqual(
                sorted(str(p.relative_to(destination)) for p in destination.rglob("*") if p.is_file()),
                ["images/setup image.png", "movie.mp4", "thumbnail.webp"],
            )

    def test_missing_documentation_image_is_reported_without_breaking_imports(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                copy_documentation_images(root, root / "output", "---\npath: basics/fixture\n---\n![missing](missing.png)")
            self.assertIn("Missing example documentation image", output.getvalue())

    def test_pruning_preserves_external_page_references_and_nested_game_resources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            example = root / "examples/basics/fixture"
            example.mkdir(parents=True)
            (example / "index.md").write_text("example")
            for filename in ("setup image.png", "thumbnail.webp", "external.png", "unused.png", "archive/texture.png"):
                path = example / filename
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"image")
            site = root / "site"
            built = site / "examples/basics/fixture/index.html"
            built.parent.mkdir(parents=True)
            built.write_text('<img src="setup%20image.png"><img srcset="thumbnail.webp 1x">')
            (site / "index.html").write_text('<img src="https://defold.com/examples/basics/fixture/external.png">')
            self.assertEqual(prune_unused_images(site, root), (1, 5))
            self.assertFalse((example / "unused.png").exists())
            self.assertTrue((example / "external.png").exists())
            self.assertTrue((example / "archive/texture.png").exists())

    def test_pruning_requires_all_example_pages_to_be_built(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            example = root / "examples/basics/fixture"
            example.mkdir(parents=True)
            (example / "index.md").write_text("example")
            with self.assertRaisesRegex(RuntimeError, "fresh Jekyll build"):
                prune_unused_images(root / "missing-site", root)


if __name__ == "__main__":
    unittest.main()
