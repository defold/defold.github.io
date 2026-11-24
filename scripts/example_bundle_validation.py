"""Validate source revisions and complete Defold HTML5 bundle inputs."""
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


REQUIRED_ARCHIVES = {'game.projectc', 'game.arci', 'game.arcd', 'game.dmanifest'}
REQUIRED_BUNDLE_FILES = ('index.html', 'dmloader.js', 'Defoldexamples.wasm', 'Defoldexamples_wasm.js')


def validate_source_archive(archive_path, sha):
    if not isinstance(sha, str) or not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise RuntimeError('Invalid examples revision in snapshot manifest')
    expected_root = 'examples-' + sha
    with zipfile.ZipFile(archive_path) as archive:
        entries = archive.infolist()
        if not entries:
            raise RuntimeError('Examples source archive is empty')
        for entry in entries:
            path = PurePosixPath(entry.filename)
            if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] != expected_root:
                raise RuntimeError('Examples source archive does not match snapshot revision {}'.format(sha))
    return expected_root


def validate_example_bundle(bundle_dir, example_path):
    bundle_dir = Path(bundle_dir)
    def fail(detail):
        raise RuntimeError('Invalid bundle for {}: {}'.format(example_path, detail))
    for name in REQUIRED_BUNDLE_FILES:
        file = bundle_dir / name
        if not file.is_file() or file.stat().st_size == 0:
            fail('missing or empty {}'.format(name))
    threaded = ('Defoldexamples_pthread.wasm', 'Defoldexamples_pthread_wasm.js')
    if any((bundle_dir / name).exists() for name in threaded):
        for name in threaded:
            file = bundle_dir / name
            if not file.is_file() or file.stat().st_size == 0:
                fail('missing or empty {}'.format(name))
    archive_dir = bundle_dir / 'archive'
    manifest_path = archive_dir / 'archive_files.json'
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        content = manifest['content']
        if not isinstance(content, list):
            raise ValueError('content must be an array')
        names = set()
        for item in content:
            name, size, pieces = item['name'], item['size'], item['pieces']
            if not isinstance(name, str) or name in names or not isinstance(size, int) or isinstance(size, bool) or size < 0:
                raise ValueError('invalid archive entry')
            names.add(name)
            if not isinstance(pieces, list) or not pieces:
                raise ValueError('missing pieces for {}'.format(name))
            offset = 0
            for piece in pieces:
                piece_name = piece['name']
                if not isinstance(piece_name, str):
                    raise ValueError('invalid piece name')
                path = PurePosixPath(piece_name)
                if path.is_absolute() or len(path.parts) != 1 or path.name in ('.', '..') or '\\' in piece_name:
                    raise ValueError('invalid archive piece path')
                file = archive_dir / piece_name
                if not file.is_file() or piece['offset'] != offset:
                    raise ValueError('missing or invalid piece {}'.format(piece_name))
                offset += file.stat().st_size
            if offset != size:
                raise ValueError('incorrect size for {}'.format(name))
        if not REQUIRED_ARCHIVES.issubset(names):
            raise ValueError('missing required game archives: {}'.format(', '.join(sorted(REQUIRED_ARCHIVES - names))))
    except (OSError, ValueError, TypeError, KeyError) as error:
        fail('invalid archive manifest or pieces ({})'.format(error))
