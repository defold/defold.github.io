import ast
import json
import os
import re
import shutil
import tempfile
import unittest
import zipfile
from contextlib import contextmanager
from pathlib import Path


class ExampleBundleImportTest(unittest.TestCase):
    def test_imports_bundle_matching_source_snapshot(self):
        source = (Path(__file__).resolve().parents[1] / 'update.py').read_text()
        tree = ast.parse(source)
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'process_examples')
        original = os.getcwd()
        with tempfile.TemporaryDirectory() as temp:
            try:
                os.chdir(temp)
                for path in ('_includes', '_data', 'examples'):
                    Path(path).mkdir()
                Path('_data/examplesindex.json').write_text('[]')
                with zipfile.ZipFile('examples-master.zip', 'w') as archive:
                    archive.writestr('examples-abc/sprite/demo/example.md', '---\ntitle: Demo\n---\n')
                with zipfile.ZipFile('examples-bundles.zip', 'w') as archive:
                    archive.writestr('manifest.json', json.dumps({'examples_sha': 'abc'}))
                    archive.writestr('bundles/sprite/demo/index.html', 'index')
                    archive.writestr('bundles/sprite/demo/game.arcd', 'bundle')

                @contextmanager
                def tmpdir():
                    with tempfile.TemporaryDirectory() as path:
                        yield path

                def rmtree(path):
                    if os.path.isdir(path):
                        shutil.rmtree(path)

                def rmmkdir(path):
                    rmtree(path)
                    os.makedirs(path)

                def unzip(path, destination):
                    with zipfile.ZipFile(path) as archive:
                        archive.extractall(destination)

                class Dedupe:
                    @staticmethod
                    def run():
                        pass

                namespace = dict(os=os, Path=Path, json=json, zipfile=zipfile, shutil=shutil, re=re,
                    EXAMPLES_ZIP='examples-master.zip', tmpdir=tmpdir, rmtree=rmtree, rmmkdir=rmmkdir,
                    unzip=unzip, find_unzipped_repo_dir=lambda root, prefix: next(str(p) for p in Path(root).iterdir() if p.is_dir() and p.name.startswith(prefix)),
                    read_as_json=lambda p: json.loads(Path(p).read_text()), load_frontmatter=lambda p: {'title': 'Demo'},
                    find_example_scripts=lambda p: [], resolve_example_scripts=lambda a, b: [],
                    makedirs=lambda p: os.makedirs(p, exist_ok=True), copy_example_scripts=lambda *a: None,
                    replace_frontmatter=lambda *a: None, read_as_string=lambda p: Path(p).read_text(),
                    copy_documentation_images=lambda *a: None, write_as_json=lambda p, d: Path(p).write_text(json.dumps(d)),
                    generate_llms_examples=lambda: None, dedupe_examples_wasm=Dedupe(), normalize_example_path=lambda p: p)
                exec(compile(ast.Module(body=[function], type_ignores=[]), 'update.py', 'exec'), namespace)
                namespace['process_examples']()
                self.assertEqual(Path('examples/sprite/demo/game.arcd').read_text(), 'bundle')
                self.assertEqual(json.loads(Path('_data/examples_build.json').read_text())['examples_sha'], 'abc')
            finally:
                os.chdir(original)


if __name__ == '__main__':
    unittest.main()
