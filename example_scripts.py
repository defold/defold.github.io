import os
import shutil
from pathlib import Path, PurePosixPath


SCRIPT_EXTENSIONS = {
    ".script",
    ".gui_script",
    ".lua",
    ".vp",
    ".fp",
    ".cp",
    ".glsl",
    ".render_script",
}

IGNORED_SCRIPT_DIRS = {
    ".deps",
    ".git",
    ".internal",
    "build",
    "builtins",
    "js-web",
    "node_modules",
}


def split_example_scripts(scripts):
    if isinstance(scripts, str):
        return [script.strip() for script in scripts.split(",") if script.strip()]
    if isinstance(scripts, list):
        return [str(script).strip() for script in scripts if str(script).strip()]
    return []


def find_example_scripts(project_dir):
    project_dir = Path(project_dir)
    scripts = []
    if not project_dir.exists():
        return scripts

    for root, dirnames, filenames in os.walk(project_dir):
        dirnames[:] = [dirname for dirname in dirnames if dirname not in IGNORED_SCRIPT_DIRS]
        root_path = Path(root)
        for filename in filenames:
            path = root_path / filename
            if path.suffix in SCRIPT_EXTENSIONS:
                scripts.append(path.relative_to(project_dir).as_posix())

    return sorted(scripts)


def resolve_example_script(script, available_scripts):
    path = PurePosixPath(script)
    if (
        not script
        or "\\" in script
        or path.is_absolute()
        or str(path) != script
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise ValueError(
            "scripts entry must be a file name or normalized project-relative path, got '{}'".format(script)
        )

    if len(path.parts) > 1:
        if script not in available_scripts:
            raise ValueError("scripts entry '{}' does not exist in the project".format(script))
        return script

    matches = [candidate for candidate in available_scripts if PurePosixPath(candidate).name == script]
    if not matches:
        raise ValueError("scripts entry '{}' does not exist in the project".format(script))
    if len(matches) > 1:
        raise ValueError(
            "scripts entry '{}' is ambiguous; use an exact project-relative path: {}".format(
                script, ", ".join(matches)
            )
        )
    return matches[0]


def resolve_example_scripts(scripts, available_scripts):
    return [
        (script, resolve_example_script(script, available_scripts))
        for script in split_example_scripts(scripts)
    ]


def example_include_name(script):
    path = PurePosixPath(script)
    suffix = path.suffix
    include_file = "{}_{}.md".format(path.stem, suffix.lstrip("."))
    return str(path.with_name(include_file))


def copy_example_scripts(project_dir, includes_dir, resolved_scripts):
    project_dir = Path(project_dir)
    includes_dir = Path(includes_dir)
    for declared_script, resolved_script in resolved_scripts:
        source = project_dir.joinpath(*PurePosixPath(resolved_script).parts)
        target = includes_dir.joinpath(*PurePosixPath(example_include_name(declared_script)).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
