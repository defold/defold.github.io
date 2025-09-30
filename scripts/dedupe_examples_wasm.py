#!/usr/bin/env python3
"""Deduplicate Defold example WebAssembly artifacts.

This script scans the example directories, moves identical `*.wasm` and
`*_wasm.js` files into a shared `examples/wasm/` cache keyed by the file's MD5,
updates each example's `dmloader.js` to load from the shared cache, and ensures
engine loader helpers point to the new locations.

Run automatically from `update.py` after importing examples or manually with
`python3 scripts/dedupe_examples_wasm.py` to shrink the published site size.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Tuple

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = ROOT / "examples"
DEDUP_DIR = EXAMPLES_DIR / "wasm"


@dataclass(frozen=True)
class Artifact:
    property_name: str
    filename: str
    suffix: str
    size_property: str


ARTIFACTS: Tuple[Artifact, ...] = (
    Artifact("wasm_file", "Defoldexamples.wasm", ".wasm", "wasm_size"),
    Artifact("wasm_pthread_file", "Defoldexamples_pthread.wasm", ".wasm", "wasm_pthread_size"),
    Artifact("wasmjs_file", "Defoldexamples_wasm.js", ".wasm.js", "wasmjs_size"),
    Artifact("wasmjs_pthread_file", "Defoldexamples_pthread_wasm.js", ".wasm.js", "wasmjs_pthread_size"),
)


def md5_digest(path: Path) -> str:
    hasher = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def ensure_absolute_url(url: str) -> str:
    if not url.startswith("/"):
        return f"/examples/wasm/{url}"
    return url


def dedupe_artifact(source: Path, artifact: Artifact) -> Tuple[str, int]:
    digest = md5_digest(source)
    hashed_name = f"{digest}{artifact.suffix}"
    target_path = DEDUP_DIR / hashed_name
    if not target_path.exists():
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target_path)
    size = target_path.stat().st_size
    # Remove the original artifact to avoid duplication.
    try:
        source.unlink()
    except FileNotFoundError:
        pass
    return ensure_absolute_url(hashed_name), size


def insert_property_block(content: str, values: Dict[str, str]) -> str:
    if "wasm_file:" in content:
        return content

    def repl(match: re.Match[str]) -> str:
        asmjs_line = match.group(0)
        block = (
            f"{asmjs_line}"
            f"    wasm_file: \"{values['wasm_file']}\",\n"
            f"    wasm_pthread_file: \"{values['wasm_pthread_file']}\",\n"
            f"    wasmjs_file: \"{values['wasmjs_file']}\",\n"
            f"    wasmjs_pthread_file: \"{values['wasmjs_pthread_file']}\",\n"
        )
        return block

    pattern = re.compile(r"    asmjs_size:\s*\d+,\n")
    if not pattern.search(content):
        raise RuntimeError("Failed to locate asmjs_size line in dmloader.js")
    return pattern.sub(repl, content, count=1)


def set_string_property(content: str, key: str, value: str) -> str:
    pattern = re.compile(rf'({re.escape(key)}:\s*")([^\"]*)(",)')
    if not pattern.search(content):
        raise RuntimeError(f"Failed to locate property {key}")
    return pattern.sub(rf"\1{value}\3", content, count=1)


def set_numeric_property(content: str, key: str, value: int) -> str:
    pattern = re.compile(rf"({key}:\\s*)(\d+)")
    if not pattern.search(content):
        return content
    return pattern.sub(rf"\1{value}", content, count=1)


def update_wasm_name_helpers(content: str) -> str:
    content = content.replace(
        "    getWasmName: function(exeName) {\n"
        "        if (Module['isWASMPthreadSupported'])\n"
        "            return exeName + '_pthread.wasm';\n"
        "        return exeName + '.wasm';\n"
        "    },",
        "    getWasmName: function(exeName) {\n"
        "        if (Module['isWASMPthreadSupported'])\n"
        "            return EngineLoader.wasm_pthread_file;\n"
        "        return EngineLoader.wasm_file;\n"
        "    },",
    )

    content = content.replace(
        "    getWasmJSName: function(exeName) {\n"
        "        if (Module['isWASMPthreadSupported'])\n"
        "            return exeName + '_pthread_wasm.js';\n"
        "        return exeName + '_wasm.js';\n"
        "    },",
        "    getWasmJSName: function(exeName) {\n"
        "        if (Module['isWASMPthreadSupported'])\n"
        "            return EngineLoader.wasmjs_pthread_file;\n"
        "        return EngineLoader.wasmjs_file;\n"
        "    },",
    )
    return content


def update_locate_file(content: str) -> str:
    pattern = re.compile(r"Module\[\"locateFile\"\]\s*=\s*function\(path, scriptDirectory\)\n\{[\s\S]+?return scriptDirectory \+ path;\n};")
    replacement = (
        "Module[\"locateFile\"] = function(path, scriptDirectory)\n"
        "{\n"
        "    if (path == \"dmengine.wasm\" || path == \"dmengine_release.wasm\" || path == \"dmengine_headless.wasm\") {\n"
        "        if (Module['isWASMPthreadSupported']) {\n"
        "            path = EngineLoader.wasm_pthread_file;\n"
        "        } else {\n"
        "            path = EngineLoader.wasm_file;\n"
        "        }\n"
        "    }\n"
        "    if (path[0] === '/' || path.startsWith('http')) {\n"
        "        return path;\n"
        "    }\n"
        "    return scriptDirectory + path;\n"
        "};"
    )
    if not pattern.search(content):
        raise RuntimeError("Failed to locate Module[\"locateFile\"] block")
    return pattern.sub(replacement, content, count=1)


def process_dmloader(dmloader_path: Path) -> bool:
    updated = False
    values: Dict[str, str] = {art.property_name: "" for art in ARTIFACTS}
    sizes: Dict[str, int] = {}

    for art in ARTIFACTS:
        artifact_path = dmloader_path.parent / art.filename
        if artifact_path.exists():
            hashed_url, size = dedupe_artifact(artifact_path, art)
            values[art.property_name] = hashed_url
            sizes[art.size_property] = size
            updated = True
        else:
            # Fallback to non-pthread variants if pthread artifacts are missing.
            if art.property_name.endswith("pthread_file"):
                fallback = art.property_name.replace("_pthread_file", "_file")
                values[art.property_name] = values.get(fallback, "")
                sizes[art.size_property] = sizes.get(art.size_property.replace("_pthread", ""), 0)

    content = dmloader_path.read_text()
    original_content = content

    content = insert_property_block(content, values)

    for art in ARTIFACTS:
        content = set_string_property(content, art.property_name, values[art.property_name])
        if art.size_property in sizes and sizes[art.size_property]:
            content = set_numeric_property(content, art.size_property, sizes[art.size_property])

    content = update_wasm_name_helpers(content)
    content = update_locate_file(content)

    if content != original_content:
        dmloader_path.write_text(content)
        updated = True

    return updated


def iter_example_dmloaders() -> Iterable[Path]:
    if not EXAMPLES_DIR.exists():
        return []
    return sorted(EXAMPLES_DIR.glob("*/**/dmloader.js"))


def run() -> bool:
    if not EXAMPLES_DIR.exists():
        raise RuntimeError("examples directory not found")

    DEDUP_DIR.mkdir(parents=True, exist_ok=True)

    dmloaders = list(iter_example_dmloaders())
    if not dmloaders:
        raise RuntimeError("no dmloader.js files found")

    changed = 0
    for dmloader in dmloaders:
        if process_dmloader(dmloader):
            changed += 1
            rel = dmloader.relative_to(ROOT)
            print(f"updated {rel}")

    if changed == 0:
        print("No changes required")
        return False

    print(f"Updated {changed} loader(s)")
    return True


def main() -> int:
    try:
        run()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
