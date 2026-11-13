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

from scripts.example_bundle_validation import validate_example_bundle, validate_source_archive


SHA_A = 'a' * 40
SHA_B = 'b' * 40


def bundle_files():
    entries = []
    result = {'index.html': b'index', 'dmloader.js': b'loader',
              'Defoldexamples.wasm': b'wasm', 'Defoldexamples_wasm.js': b'engine'}
    for suffix in ('projectc', 'arci', 'arcd', 'dmanifest'):
        data = ('data-' + suffix).encode()
        name = 'game0.' + suffix
        result['archive/' + name] = data
        entries.append({'name': 'game.' + suffix, 'size': len(data), 'pieces': [{'name': name, 'offset': 0}]})
    result['archive/archive_files.json'] = json.dumps({'content': entries}).encode()
    return result


class ExampleBundleImportTest(unittest.TestCase):
    def setUp(self):
        self.original = os.getcwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)
        for path in ('_includes/examples', '_data', 'examples/sprite/demo', 'examples/sprite/other'):
            Path(path).mkdir(parents=True)
        Path('_data/examplesindex.json').write_text('[]')
        Path('_data/examples_build.json').write_text('{"examples_sha":"old"}')
        Path('_includes/examples/keep.txt').write_text('unchanged')
        for example in ('demo', 'other'):
            Path('examples/sprite', example, 'keep.txt').write_text('unchanged')
        self.make_source(SHA_A)
        self.make_snapshot()

    def tearDown(self):
        os.chdir(self.original)
        self.temp.cleanup()

    def make_source(self, sha):
        with zipfile.ZipFile('examples-master.zip', 'w') as archive:
            for example in ('demo', 'other'):
                archive.writestr('examples-{}/sprite/{}/example.md'.format(sha, example), '---\ntitle: Demo\n---\n')

    def make_snapshot(self, remove=None):
        with zipfile.ZipFile('examples-bundles.zip', 'w') as archive:
            archive.writestr('manifest.json', json.dumps({'examples_sha': SHA_A}))
            for example in ('demo', 'other'):
                for name, content in bundle_files().items():
                    if (example, name) != remove:
                        archive.writestr('bundles/sprite/{}/{}'.format(example, name), content)

    def importer(self):
        source = (Path(__file__).resolve().parents[1] / 'update.py').read_text()
        tree = ast.parse(source)
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'process_examples')
        @contextmanager
        def tmpdir():
            with tempfile.TemporaryDirectory() as path:
                yield path
        def rmtree(path):
            if os.path.isdir(path): shutil.rmtree(path)
        def rmmkdir(path):
            rmtree(path)
            os.makedirs(path)
        def unzip(path, destination):
            with zipfile.ZipFile(path) as archive: archive.extractall(destination)
        class Dedupe:
            @staticmethod
            def run(): pass
        namespace = dict(os=os, Path=Path, json=json, zipfile=zipfile, shutil=shutil, re=re,
            EXAMPLES_ZIP='examples-master.zip', tmpdir=tmpdir, rmtree=rmtree, rmmkdir=rmmkdir,
            validate_source_archive=validate_source_archive, validate_example_bundle=validate_example_bundle,
            unzip=unzip, read_as_json=lambda p: json.loads(Path(p).read_text()),
            load_frontmatter=lambda p: {'title': 'Demo'}, find_example_scripts=lambda p: [],
            resolve_example_scripts=lambda a, b: [], makedirs=lambda p: os.makedirs(p, exist_ok=True),
            copy_example_scripts=lambda *a: None, replace_frontmatter=lambda *a: None,
            read_as_string=lambda p: Path(p).read_text(), copy_documentation_images=lambda *a: None,
            write_as_json=lambda p, d: Path(p).write_text(json.dumps(d)),
            generate_llms_examples=lambda: None, dedupe_examples_wasm=Dedupe(), normalize_example_path=lambda p: p)
        exec(compile(ast.Module(body=[function], type_ignores=[]), 'update.py', 'exec'), namespace)
        return namespace['process_examples']

    def assert_preserved(self):
        self.assertEqual(Path('_includes/examples/keep.txt').read_text(), 'unchanged')
        for example in ('demo', 'other'):
            self.assertEqual(Path('examples/sprite', example, 'keep.txt').read_text(), 'unchanged')
        self.assertEqual(json.loads(Path('_data/examples_build.json').read_text())['examples_sha'], 'old')

    def test_imports_bundle_matching_source_snapshot(self):
        self.importer()()
        self.assertEqual(Path('examples/sprite/demo/archive/game0.arcd').read_bytes(), b'data-arcd')
        self.assertEqual(json.loads(Path('_data/examples_build.json').read_text())['examples_sha'], SHA_A)

    def test_mismatched_cached_source_does_not_change_existing_examples(self):
        self.make_source(SHA_B)
        with self.assertRaisesRegex(RuntimeError, 'does not match snapshot revision'):
            self.importer()()
        self.assert_preserved()

    def test_incomplete_bundle_does_not_change_any_examples(self):
        for missing in ('dmloader.js', 'Defoldexamples.wasm', 'Defoldexamples_wasm.js', 'archive/game0.arcd', 'archive/archive_files.json'):
            with self.subTest(missing=missing):
                self.make_snapshot(remove=('other', missing))
                with self.assertRaisesRegex(RuntimeError, 'Invalid bundle for sprite/other'):
                    self.importer()()
                self.assert_preserved()

    def test_split_archive_pieces_are_checked(self):
        root = Path('split')
        root.mkdir()
        files = bundle_files()
        manifest = json.loads(files['archive/archive_files.json'])
        arcd = next(item for item in manifest['content'] if item['name'] == 'game.arcd')
        data = files.pop('archive/game0.arcd')
        files['archive/game0.arcd'] = data[:2]
        files['archive/game1.arcd'] = data[2:]
        arcd['pieces'] = [{'name': 'game0.arcd', 'offset': 0}, {'name': 'game1.arcd', 'offset': 2}]
        files['archive/archive_files.json'] = json.dumps(manifest).encode()
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        validate_example_bundle(root, 'sprite/demo')
        (root / 'archive/game1.arcd').unlink()
        with self.assertRaisesRegex(RuntimeError, 'game1.arcd'):
            validate_example_bundle(root, 'sprite/demo')


if __name__ == '__main__':
    unittest.main()
