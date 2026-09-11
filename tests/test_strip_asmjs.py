from pathlib import Path
import tempfile
import unittest

from scripts.strip_asmjs import run


INLINE_LOADER = """function load_engine() {
    var engineJS = document.createElement('script');
    if (Module['isWASMSupported']) {
        engineJS.src = 'Demo_wasm.js';
    } else {
        engineJS.src = 'Demo_asmjs.js';
    }
    document.head.appendChild(engineJS);
}
"""


class StripAsmjsTests(unittest.TestCase):
    def make_bundle(self, root, loader=INLINE_LOADER):
        root.mkdir(parents=True, exist_ok=True)
        for name in ("Demo.wasm", "Demo_wasm.js", "Demo_asmjs.js", "dmloader.js"):
            (root / name).write_bytes(b"runtime fixture")
        (root / "index.html").write_text(loader)
        archive = root / "archive"
        archive.mkdir(exist_ok=True)
        (archive / "game.arcd").write_bytes(b"game resources")

    def test_reimport_removes_fallback_and_preserves_wasm_and_game_resources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_bundle(root)
            preserved = {name: (root / name).read_bytes() for name in ("Demo.wasm", "Demo_wasm.js", "archive/game.arcd")}
            result = run(root)
            cleaned = (root / "index.html").read_text()
            self.assertEqual(result, {"removed": 1, "bytes": 15, "updated": 1})
            self.assertNotIn("_asmjs.js", cleaned)
            self.assertIn("engineJS.src = 'Demo_wasm.js'", cleaned)
            self.assertIn("WebAssembly is required", cleaned)
            self.assertEqual(run(root), {"removed": 0, "bytes": 0, "updated": 0})

            self.make_bundle(root)
            run(root)
            self.assertEqual((root / "index.html").read_text(), cleaned)
            for name, data in preserved.items():
                self.assertEqual((root / name).read_bytes(), data)

    def test_missing_wasm_replacement_prevents_all_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_bundle(root / "valid")
            self.make_bundle(root / "invalid")
            (root / "invalid/Demo.wasm").unlink()
            with self.assertRaisesRegex(RuntimeError, "Missing WebAssembly replacement"):
                run(root)
            for bundle in ("valid", "invalid"):
                self.assertTrue((root / bundle / "Demo_asmjs.js").is_file())
                self.assertEqual((root / bundle / "index.html").read_text(), INLINE_LOADER)

    def test_unknown_fallback_prevents_deleting_a_still_referenced_engine(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            unknown = "loadScript('Demo_asmjs.js');"
            self.make_bundle(root, unknown)
            with self.assertRaisesRegex(RuntimeError, "Unrecognized asm.js fallback"):
                run(root)
            self.assertTrue((root / "Demo_asmjs.js").is_file())
            self.assertEqual((root / "index.html").read_text(), unknown)

    def test_built_site_is_not_modified_when_processing_repository(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_bundle(root / "_site/demo")
            self.assertEqual(run(root), {"removed": 0, "bytes": 0, "updated": 0})
            self.assertTrue((root / "_site/demo/Demo_asmjs.js").is_file())


if __name__ == "__main__":
    unittest.main()
