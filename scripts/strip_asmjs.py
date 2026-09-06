"""Keep published HTML5 bundles on WebAssembly, including older imported demos."""

import argparse
import os
from pathlib import Path
import re
import textwrap


ROOT = Path(__file__).resolve().parents[1]
ASMJS_REFERENCE = re.compile(r"_asmjs\.js|\b(?:loadAsmJsAsync|asmjs_size|asmjs_sha1)\b")
FALLBACK = re.compile(
    r"(?P<indent>^[ \t]*)if \((?P<supported>Module\[['\"]isWASMSupported['\"]\]|isWASMSupported)\) \{\n"
    r"(?P<wasm>[^{}]+)\n(?P=indent)\} else \{\n(?P<asm>[^{}]+)\n(?P=indent)\}",
    re.MULTILINE,
)


def wasm_only_loader(source):
    def remove_fallback(match):
        if not ASMJS_REFERENCE.search(match["asm"]):
            return match[0]
        indent = match["indent"]
        body = textwrap.indent(textwrap.dedent(match["wasm"]).strip(), indent)
        return (
            indent + "if (!(" + match["supported"] + ")) {\n"
            + indent + '    throw new Error("WebAssembly is required to run this demo.");\n'
            + indent + "}\n" + body
        )

    source = FALLBACK.sub(remove_fallback, source)
    source = re.sub(r"^[ \t]*asmjs_(?:size|sha1):[^\n]*\n", "", source, flags=re.MULTILINE)
    source = re.sub(
        r"^[ \t]*loadAsmJsAsync: function\(exeName\) \{[^{}]*\},\n",
        "", source, flags=re.MULTILINE,
    )
    source = source.replace("(asm.js or wasm.js", "(wasm.js")
    if ASMJS_REFERENCE.search(source):
        raise RuntimeError("Unrecognized asm.js fallback; rebuild the demo for WebAssembly")
    return source


def run(root=ROOT):
    root = Path(root)
    updates = []
    removals = []
    for directory, directories, filenames in os.walk(root):
        directories[:] = [name for name in directories if not name.startswith(".") and name not in {"_site", "vendor", "node_modules"}]
        bundle = Path(directory)
        asmjs_files = sorted(bundle / name for name in filenames if name.endswith("_asmjs.js"))
        if "dmloader.js" not in filenames and not asmjs_files:
            continue

        for asmjs in asmjs_files:
            base = asmjs.name[:-len("_asmjs.js")]
            for suffix in (".wasm", "_wasm.js"):
                replacement = bundle / (base + suffix)
                if not replacement.is_file():
                    raise RuntimeError(f"Missing WebAssembly replacement for {asmjs}: {replacement}")
            removals.append(asmjs)

        for name in filenames:
            if not name.endswith((".html", ".js")) or name.endswith(("_asmjs.js", "_wasm.js", ".wasm.js")):
                continue
            path = bundle / name
            source = path.read_text(encoding="utf-8")
            if not ASMJS_REFERENCE.search(source):
                continue
            try:
                updated = wasm_only_loader(source)
            except RuntimeError as error:
                raise RuntimeError(f"{path}: {error}") from error
            if updated != source:
                updates.append((path, updated))

    # Validate every bundle before changing any loader or deleting an engine.
    saved = sum(path.stat().st_size for path in removals)
    for path, source in updates:
        path.write_text(source, encoding="utf-8")
    for path in removals:
        path.unlink()
    return {"removed": len(removals), "bytes": saved, "updated": len(updates)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=ROOT)
    result = run(parser.parse_args().directory)
    print(f"Removed {result['removed']} asm.js engines ({result['bytes'] / 1024**2:.2f} MiB); updated {result['updated']} loaders")
