#!/usr/bin/env python

from urllib.request import urlopen
from urllib.parse import urlparse
import zipfile
import os
import sys
import shutil
import fnmatch
import json
import tempfile
import re
import subprocess
import requests
import hashlib
import yaml

from llms import LLMS_DIR, generate_llms_manuals, generate_llms_apis, generate_llms_examples, path_to_manuals_anchor
from utils import list_files, read_as_json, read_as_string, rmtree, write_as_string
from scripts import dedupe_examples_wasm
from argparse import ArgumentParser
from contextlib import contextmanager


SHA1 = {}

DOCS_ZIP = "doc-master.zip"
EXAMPLES_ZIP = "examples-master.zip"
CODEPAD_ZIP = "codepad-master.zip"
ASSETPORTAL_ZIP = "asset-portal-master.zip"
GAMESSHOWCASE_ZIP = "games-showcase-master.zip"

EXAMPLES_DEFOLD_CHANNEL = "beta"
EXAMPLES_BUILD_SERVER = "https://build-stage.defold.com/"
EXAMPLE_CODE_FILE_PATTERNS = "*.script|*.gui_script|*.lua|*.vp|*.fp|*.cp|*.glsl|*.render_script"

ASSETINDEX_JSON = os.path.join("_data", "assetindex.json")
GAMES_JSON = os.path.join("_data", "games.json")
AUTHORINDEX_JSON = os.path.join("_data", "authorindex.json")
TAGINDEX_JSON = os.path.join("_data", "tagindex.json")
PLATFORMINDEX_JSON = os.path.join("_data", "platformindex.json")

REF_DATA_DIR = os.path.join("_data", "ref")


ASSET_MD_FRONTMATTER = """---
layout: asset
asset: {}
title: {}
description: {}
opengraph_image: {}
twitter_image: {}
---
"""

AUTHOR_MD_FRONTMATTER = """---
layout: author
author: {}
title: {}
---
"""

TAG_MD_FRONTMATTER = """---
layout: assetportal
tag: {}
title: {}
---
"""

TAG_SORT_MD_FRONTMATTER = """---
layout: assetportal
tag: {}
title: {}
sort: {}
---
"""

REFDOC_MD_FRONTMATTER = """---
layout: api
branch: {}
ref: {}
api_language: {}
title: API reference ({})
type: {}
{}---
"""
REFDOC_MD_BODY = "{% include anchor_headings.html html=content %}"

EXAMPLES_ENGINE_LOADER = """
        CUSTOM_PARAMETERS.archive_location_filter = function(path) { return ("/examples/archive" + path); };
        CUSTOM_PARAMETERS.engine_arguments = [ '--config=examples.start={{ page.collection }}', '--verify-graphics-calls=false' ];
        CUSTOM_PARAMETERS.resize_window_callback = function() {};
        EngineLoader.load("canvas", "/examples/Defoldexamples");
"""

@contextmanager
def tmpdir():
    name = tempfile.mkdtemp()
    try:
        yield name
    finally:
        shutil.rmtree(name)

def rmmkdir(dir):
    rmtree(dir)
    os.mkdir(dir)

def rmcopytree(src, dst):
    rmtree(dst)
    shutil.copytree(src, dst)

def copytree(src, dst, overwrite = False):
    if os.path.isdir(src):
        if not os.path.isdir(dst):
            os.makedirs(dst)
        for f in os.listdir(src):
            copytree(os.path.join(src, f), os.path.join(dst, f), overwrite)
    elif overwrite or not os.path.exists(dst):
        shutil.copyfile(src, dst)

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def call(args):
    print(args)
    ret = os.system(args)
    if ret != 0:
        sys.exit(1)

def unzip(filename, destination):
    print("Unpacking {}".format(filename))
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(destination)
    zip_ref.close()

def create_markdown():
    from markdown import Markdown
    return Markdown(extensions=['markdown.extensions.fenced_code','markdown.extensions.def_list', 'markdown.extensions.codehilite','markdown.extensions.tables'])


def download_file(url, destination, filename=None):
    if not filename:
        filename = url.rsplit('/', 1)[-1]
    path = os.path.join(destination, filename)
    if os.path.exists(path):
        print("File %s already exists" % (path))
        sys.exit(1)
    print("Downloading {} to {}".format(url, path))
    try:
        f = urlopen(url)
        with open(path, 'wb') as output:
            output.write(f.read())
    except:
        path = None
    return path


def download_string(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Unable to download from %s (%d)" % (url, response.status_code))
        return None
    return response.text


def download_json(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Unable to download from %s (%d)" % (url, response.status_code))
        return None
    return response.json()


def get_sha1(branch = "stable"):
    global SHA1
    if not SHA1.get(branch):
        info = download_json("https://d.defold.com/{}/info.json".format(branch))
        SHA1[branch] = info["sha1"]
    return SHA1[branch]


def get_bob_filename(sha1):
    return "bob_{}.jar".format(sha1)


def download_bob(sha1):
    bob_filename = get_bob_filename(sha1)
    if not os.path.exists(bob_filename):
        download_file("http://d.defold.com/archive/{}/bob/bob.jar".format(sha1), ".", bob_filename)

def find_file(root_dir, file_pattern):
    for root, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, file_pattern):
                return os.path.join(root, filename)
    return None

def find_files(root_dir, file_patterns):
    matches = []
    patterns = file_patterns.split("|")
    for pattern in patterns:
        for root, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if fnmatch.fnmatch(filename, pattern):
                    matches.append(os.path.join(root, filename))
    matches.sort()
    return matches

def example_include_name(filename):
    file, ext = os.path.splitext(os.path.basename(filename))
    return file + "_" + ext.replace(".", "") + ".md"

def split_example_scripts(scripts):
    if isinstance(scripts, str):
        return [s.strip() for s in scripts.split(",") if s.strip()]
    if isinstance(scripts, list):
        return [str(s).strip() for s in scripts if str(s).strip()]
    return []

def write_as_json(filename, data, ensure_ascii=True):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=ensure_ascii)

def write_lines(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)

def replace_in_file(filename, old, new, flags=None):
    with open(filename) as f:
        if flags is None:
            content = re.sub(old, new, f.read())
        else:
            content = re.sub(old, new, f.read(), flags=flags)

    with open(filename, "w") as f:
        f.write(content)

def replace_in_first_line(filename, old, new, flags=None):
    with open(filename) as f:
        lines = f.readlines()
        if lines:
            if flags is None:
                lines[0] = re.sub(old, new, lines[0])
            else:
                lines[0] = re.sub(old, new, lines[0], flags=flags)

    with open(filename, "w") as f:
        f.writelines(lines)

def append_to_file(filename, s):
    with open(filename, "a") as f:
        f.write(s)

def dict_to_yaml(d):
    return yaml.dump(d, allow_unicode=True, width=sys.maxsize, default_flow_style=False)

def load_frontmatter(filename):
    parts = read_as_string(filename).split("---", maxsplit = 2)
    return yaml.safe_load(parts[1])

def normalize_example_path(path):
    path = path.strip().strip("/")
    if not path:
        return None
    parts = path.split("/")
    if len(parts) < 2:
        return None
    if parts[0].startswith("."):
        return None
    return "/".join(parts[:2])

def parse_changed_examples(value):
    if not value:
        return []
    paths = []
    for item in re.split(r"[\s,]+", value):
        normalized = normalize_example_path(item)
        if normalized:
            paths.append(normalized)
    return sorted(set(paths))

def parse_changed_examples_json(value):
    if not value or value == "null":
        return []
    try:
        data = json.loads(value)
    except json.JSONDecodeError:
        return parse_changed_examples(value)
    if isinstance(data, str):
        return parse_changed_examples(data)
    if not isinstance(data, list):
        return []
    paths = []
    for item in data:
        normalized = normalize_example_path(str(item))
        if normalized:
            paths.append(normalized)
    return sorted(set(paths))

def find_unzipped_repo_dir(root, prefix):
    for entry in os.listdir(root):
        path = os.path.join(root, entry)
        if os.path.isdir(path) and entry.startswith(prefix):
            return path
    return None

def replace_frontmatter(filename, d):
    parts = read_as_string(filename).split("---", maxsplit = 2)
    content = parts[2].strip()
    frontmatter = dict_to_yaml(d)
    content = "---\n%s\n---\n\n%s" % (frontmatter, content)
    write_as_string(filename, content)

def append_frontmatter(filename, d):
    s = read_as_string(filename)
    if s.startswith("---"):
        parts = s.split("---", maxsplit = 2)
        d.update(yaml.safe_load(parts[1]))
        content = parts[2].strip()
        frontmatter = dict_to_yaml(d).strip()
        write_as_string(filename, "---\n%s\n---\n\n%s" % (frontmatter, content))
    else:
        content = s
        frontmatter = dict_to_yaml(d).strip()
        write_as_string(filename, "---\n%s\n---\n\n%s" % (frontmatter, content))


def process_doc_file(file, locale):
    replace_in_file(file, r"({{{?)(.*?)(}}}?)", r"{% raw %}\1\2\3{% endraw %}")
    replace_in_file(file, r"{% raw %}({{{?)(.*?include\..*?)(}}}?){% endraw %}", r"\1\2\3")
    replace_in_file(file, r"{\s*srcset=.*?}", r"")
    replace_in_file(file, r"::: sidenote(.*?):::", r"<div class='sidenote' markdown='1'>\1</div>", flags=re.DOTALL)
    replace_in_file(file, r"::: important(.*?):::", r"<div class='important' markdown='1'>\1</div>", flags=re.DOTALL)
    replace_in_file(file, r"\((.*?)#_(.*?)\)", r"(\1#\2)")
    replace_in_file(file, r":\[.*?\]\(\.\.\/(.*?)\)", r"{% include \1 %}")
    replace_in_file(file, r"\!\[.*?\]\((.*?)\){width=(.*) \.left}", r"<img src='../\1' width='\2'/>")
    replace_in_file(file, r"{\.left}", r"")
    replace_in_file(file, r"{\.icon}", r"")
    replace_in_file(file, r"{\.inline}", r"")
    replace_in_file(file, r"{\.mark}", r"")
    # replace_in_file(file, r"\!\[(.*?)\]\((.*?)\)\{\.inline\}", r"<span style='display: inline'>![\1](\2)</span>")
    replace_in_file(file, r"\(images\/", r"(../images/")
    replace_in_file(file, r"\(\.\.\/shared\/", r"(/shared/")
    replace_in_file(file, r"\{\% include shared\/(.*?)\.md(.*?)\%\}", r"{}".format("{% include shared/" + locale + "/\\1.md\\2%}"))

def generate_toc(file):
    data = read_as_string(file)
    lines = data.splitlines()
    toc = []
    within_comment = False
    for line in lines:
        if line.strip().startswith("```"):
            within_comment = not within_comment
        elif not within_comment and (line.startswith("# ") or line.startswith("## ") or line.startswith("### ")):
            heading = line
            heading = heading.replace("#", "")
            heading = heading.replace("'", "")
            heading = heading.replace("`", "")
            heading = heading.replace("\"", "")
            heading = heading.strip()
            # note: there is some additional stripping done in manual.html
            toc.append(heading)
    return toc


def get_locale_specific_dir(locale, dir):
    if locale != "en":
        dir = os.path.join(locale, dir)
    return dir


def get_doc_locale(path, default="en"):
    parts = os.path.normpath(path).split(os.sep)
    for part in reversed(parts[:-1]):
        if re.fullmatch(r"[a-z]{2}(?:-[A-Za-z0-9]+)?", part):
            return part
    return default


def get_api_language(info, default="Lua"):
    api_language = info.get("api_language") or info.get("language")
    if not api_language:
        api_language = default
    info["api_language"] = api_language
    info.pop("language", None)
    return api_language


def get_index_item_locales(item, locales):
    item_locales = []
    if not item["path"].startswith("http"):
        path = item["path"][1:]
        # foo/bar/#anchor -> foo/bar
        # foo/bar#anchor -> foo/bar
        path = re.sub(r"/?\#.*", "", path)
        for locale in locales["languages"].keys():
            if os.path.exists(get_locale_specific_dir(locale, path + ".md")):
                item_locales.append(locale)
    return item_locales

def update_file_links_with_locale(filename, pattern, locale):
    # Open the file and read its content
    with open(filename, 'r') as f:
        content = f.read()
    
    def is_valid_path_and_locale(path, locale):
        # Normalize the path to ensure it doesn't end with a slash
        normalized_path = path.rstrip('/').lstrip('/')
        if os.path.exists(os.path.join(locale, normalized_path + ".md")) or os.path.exists(os.path.join(locale, normalized_path)):
            return True
        return False

    
    # Use regex to find all patterns and update them if valid
    def replacement(match):
        path = match.group(0)
        # Check if the path exists and has the specified locale
        if is_valid_path_and_locale(path, locale):
            return '/{}/{}'.format(locale, path.lstrip('/'))
        else:
            return path
    
    # Compile the pattern and substitute
    compiled_pattern = re.compile(pattern)
    updated_content = compiled_pattern.sub(replacement, content)
    
    # Optionally, write the updated content back to the file or return it
    with open(filename, 'w') as f:
        f.write(updated_content)



def include_matched_file(match):
    path = os.path.join("_includes", match.group(1))
    if os.path.exists(path):
        contents = read_as_string(path).replace("\\", "\\\\")
        if match.group(2):
            # find all variable pairs in the match, i.e. key='value'
            variables = re.findall(r"(\w+)=['\"]([^'\"]+)['\"]", match.group(2))
            for key, value in variables:
                contents = contents.replace("{{ include." + key + " }}", value)
        return contents
    else:
        print("include_matched_file: file {} does not exists".format(path))
        sys.exit(1)

LEARN_TAG_PRIORITY = [
    "manual",
    "tutorial",
    "video",
    "course",
    "onboarding",
    "beginner",
    "migration",
    "unity",
    "godot",
    "unreal",
    "gamemaker",
    "flash",
    "architecture",
    "workflow",
    "project",
    "scripting",
    "components",
    "gameplay",
    "input",
    "ui-art",
    "two-d",
    "three-d",
    "rendering",
    "shaders",
    "physics",
    "assets",
    "animation",
    "audio",
    "platform",
    "mobile",
    "android",
    "ios",
    "web",
    "html5",
    "desktop",
    "windows",
    "linux",
    "macos",
    "console",
    "team",
    "editor",
    "debugging",
    "profiling",
    "performance",
    "optimization",
    "network",
    "multiplayer",
    "native",
    "extensions",
    "monetization",
    "ads",
    "iap",
    "practical"
]

LEARN_TAG_KEYWORDS = [
    ("onboarding", ["install", "introduction", "getting started", "first hour", "first 15", "start here"]),
    ("beginner", ["beginner", "new to", "first project"]),
    ("migration", ["migration", "migrate", "moving from", "porting", "unity", "godot", "unreal", "gamemaker", "flash"]),
    ("unity", ["unity"]),
    ("godot", ["godot"]),
    ("unreal", ["unreal"]),
    ("gamemaker", ["gamemaker"]),
    ("flash", ["flash"]),
    ("architecture", ["building blocks", "architecture", "addressing", "message passing", "application lifecycle"]),
    ("workflow", ["workflow", "pipeline", "tooling", "editor script", "project setup"]),
    ("project", ["project setup", "project settings", "game.project", "libraries"]),
    ("scripting", ["lua", "script", "module", "message", "addressing", "api reference"]),
    ("components", ["component", "game object", "collection", "factory", "proxy"]),
    ("gameplay", ["gameplay", "movement", "camera", "input", "controller", "state"]),
    ("ui-art", ["gui", "ui ", "atlas", "tile", "sprite", "font", "layout", "art", "graphics"]),
    ("two-d", ["2d", "sprite", "tilemap", "tile map", "flipbook"]),
    ("three-d", ["3d", "model", "mesh", "rig", "camera", "material"]),
    ("rendering", ["render", "shader", "material", "post processing", "pipeline"]),
    ("shaders", ["shader", "shadertoy", "post effect", "post effects"]),
    ("physics", ["physics", "collision", "kinematic", "box2d"]),
    ("assets", ["asset", "resource", "texture", "font", "model", "atlas"]),
    ("animation", ["animation", "spine", "flipbook"]),
    ("audio", ["audio", "sound", "music"]),
    ("platform", ["platform", "bundle", "bundling", "build", "release", "html5", "android", "ios", "desktop", "console", "web"]),
    ("mobile", ["android", "ios", "mobile"]),
    ("android", ["android"]),
    ("ios", ["ios"]),
    ("web", ["html5", "web"]),
    ("html5", ["html5"]),
    ("desktop", ["windows", "linux", "macos", "desktop"]),
    ("windows", ["windows"]),
    ("linux", ["linux"]),
    ("macos", ["macos", "mac os"]),
    ("console", ["nintendo", "playstation", "xbox", "console"]),
    ("team", ["team", "version control", "collaboration", "studio", "evaluation"]),
    ("editor", ["editor", "shortcuts", "preferences", "scriptable editor"]),
    ("debugging", ["debug", "error", "logging", "crash"]),
    ("profiling", ["profiler", "profiling"]),
    ("performance", ["performance", "memory", "cpu", "gpu"]),
    ("optimization", ["optimization", "optimize"]),
    ("network", ["network", "socket", "http", "websocket"]),
    ("multiplayer", ["multiplayer"]),
    ("native", ["native", "c++", "java", "objc"]),
    ("extensions", ["extension", "ext.manifest", "library"]),
    ("monetization", ["monetization", "iap", "ad ", "ads", "in-app purchase"]),
    ("ads", [" ad ", "ads", "admob", "advertising"]),
    ("iap", ["iap", "in-app purchase"])
]

LEARN_MANUAL_SECTION_TAGS = {
    "Basics": ["onboarding", "beginner", "workflow"],
    "Building blocks": ["architecture", "components", "scripting"],
    "Workflow": ["workflow", "editor", "team"],
    "Scripting": ["scripting", "architecture"],
    "Graphics": ["ui-art", "two-d", "three-d", "rendering"],
    "Asset Pipeline": ["assets", "workflow"],
    "Physics": ["physics", "gameplay"],
    "Audio": ["audio"],
    "Input": ["gameplay", "input"],
    "GUI": ["ui-art", "two-d"],
    "Platform-specific": ["platform", "mobile", "web", "desktop"],
    "Networking": ["network", "multiplayer"],
    "Optimization": ["optimization", "performance", "profiling"],
    "Debugging": ["debugging", "profiling"],
    "Native extensions": ["native", "extensions", "scripting"]
}


def normalize_learn_path_key(path):
    path = (path or "").strip()
    if not path:
        return ""
    if path.endswith("/"):
        path = path[:-1]
    return path.lower()


def normalize_learn_tag(tag):
    value = (tag or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value


def normalize_learn_tags(tags):
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        tags = []
    normalized = []
    seen = set()
    for tag in tags or []:
        value = normalize_learn_tag(tag)
        if value and value not in seen:
            normalized.append(value)
            seen.add(value)
    return normalized


def sort_learn_tags(tags):
    priority = {tag: index for index, tag in enumerate(LEARN_TAG_PRIORITY)}
    return sorted(tags, key=lambda tag: (priority.get(tag, len(LEARN_TAG_PRIORITY)), tag))


def collect_existing_learn_tags(index):
    existing = {
        "manuals": {},
        "tutorials": {},
        "videos": {},
        "courses": {}
    }

    navigation = index.get("navigation", {})
    for section in navigation.get("manuals", []):
        for item in section.get("items", []):
            key = normalize_learn_path_key(item.get("path"))
            tags = normalize_learn_tags(item.get("tags"))
            if key and tags:
                existing["manuals"][key] = tags

    for section_name in ["tutorials", "videos", "courses"]:
        for item in navigation.get(section_name, []):
            key = normalize_learn_path_key(item.get("path"))
            tags = normalize_learn_tags(item.get("tags"))
            if key and tags:
                existing[section_name][key] = tags

    return existing


def infer_learn_tags(surface, item, section_name=""):
    name = (item.get("name") or "").lower()
    description = (item.get("description") or "").lower()
    author = (item.get("author") or "").lower()
    path = normalize_learn_path_key(item.get("path"))
    text = " ".join([name, description, author, path, (section_name or "").lower()])

    tags = []
    if surface == "manuals":
        tags.append("manual")
    elif surface == "tutorials":
        tags.extend(["tutorial", "practical"])
    elif surface == "videos":
        tags.extend(["video", "practical"])
    elif surface == "courses":
        tags.extend(["course", "practical"])

    for section_key, section_tags in LEARN_MANUAL_SECTION_TAGS.items():
        if surface == "manuals" and section_key.lower() in (section_name or "").lower():
            tags.extend(section_tags)

    for tag, keywords in LEARN_TAG_KEYWORDS:
        for keyword in keywords:
            if keyword in text:
                tags.append(tag)
                break

    return sort_learn_tags(normalize_learn_tags(tags))


def apply_learn_tags(index, existing_tags):
    navigation = index.get("navigation", {})

    for section in navigation.get("manuals", []):
        section_name = section.get("name", "")
        for item in section.get("items", []):
            key = normalize_learn_path_key(item.get("path"))
            tags = normalize_learn_tags(item.get("tags"))
            if not tags:
                tags = existing_tags.get("manuals", {}).get(key, [])
            if not tags:
                tags = infer_learn_tags("manuals", item, section_name)
            item["tags"] = sort_learn_tags(normalize_learn_tags(tags))

    for section_name in ["tutorials", "videos", "courses"]:
        for item in navigation.get(section_name, []):
            key = normalize_learn_path_key(item.get("path"))
            tags = normalize_learn_tags(item.get("tags"))
            if not tags:
                tags = existing_tags.get(section_name, {}).get(key, [])
            if not tags:
                tags = infer_learn_tags(section_name, item)
            item["tags"] = sort_learn_tags(normalize_learn_tags(tags))



def process_docs(download = False):
    with tmpdir() as tmp_dir:
        DOC_DIR=os.environ.get('DM_DOC_DIR', None)
        if not DOC_DIR:
            if download:
                print("Downloading docs...")
                if os.path.exists(DOCS_ZIP):
                    os.remove(DOCS_ZIP)
                download_file("https://github.com/defold/doc/archive/master.zip", ".", DOCS_ZIP)

            if not os.path.exists(DOCS_ZIP):
                print("File {} does not exists".format(DOCS_ZIP))
                sys.exit(1)

            print(f"Unzipping {DOCS_ZIP} to {tmp_dir}...")
            shutil.copyfile(DOCS_ZIP, os.path.join(tmp_dir, DOCS_ZIP))
            unzip(os.path.join(tmp_dir, DOCS_ZIP), tmp_dir)
            DOC_DIR = os.path.join(tmp_dir, "doc-master")

        print("Processing docs")

        print("...locales")
        locales = read_as_json(os.path.join(DOC_DIR, "docs", "languages.json"))
        locale_list = []
        for locale in locales["languages"].keys():
            locale_data = locales["languages"][locale]
            if locale_data["active"]:
                locale_data["locale"] = locale
                if locale == "en":
                    locale_data["urlprefix"] = ""
                else:
                    locale_data["urlprefix"] = locale
                locale_list.append(locale_data)
        write_as_json(os.path.join("_data", "localeindex.json"), locale_list)

        print("...index")
        index_file = os.path.join("_data", "learnindex.json")
        existing_learn_tags = {
            "manuals": {},
            "tutorials": {},
            "videos": {},
            "courses": {}
        }
        if os.path.exists(index_file):
            existing_learn_tags = collect_existing_learn_tags(read_as_json(index_file))
        if os.path.exists(index_file):
            os.remove(index_file)
        shutil.copyfile(os.path.join(DOC_DIR, "docs", "en", "en.json"), index_file)
        index = read_as_json(index_file)
        apply_learn_tags(index, existing_learn_tags)

        for locale in locales["languages"].keys():
            print("...manuals ({})".format(locale))
            manuals_src_dir = os.path.join(DOC_DIR, "docs", locale, "manuals")
            if os.path.exists(manuals_src_dir):
                manuals_dst_dir = get_locale_specific_dir(locale, "manuals")
                rmcopytree(manuals_src_dir, manuals_dst_dir)
                for filename in find_files(manuals_dst_dir, "*.md"):
                    process_doc_file(filename, locale)
                    # update front matter
                    toc = generate_toc(filename)
                    append_frontmatter(filename, {
                        "layout": "manual",
                        "locale": locale,
                        "github": "https://github.com/defold/doc",
                        "toc": toc,
                    })
                    if locale == "en":
                        # preprocess docs pages for llms-full.txt to a temporary folder _llms/
                        contents = read_as_string(filename)
                        if "This manual has been replaced by the" in contents or "This manual has moved" in contents or "This manual has been moved" in contents:
                            pass
                        else:
                            target_dir = os.path.join(LLMS_DIR, manuals_dst_dir)
                            os.makedirs(target_dir, exist_ok=True)
                            target_file = os.path.join(LLMS_DIR, filename)
                            with open(target_file, "w") as f:
                                f.write(contents)
                            # include files
                            replace_in_file(target_file, r"\{\% include (shared\/.*?\.md)(.+?)\%\}", include_matched_file)
                            # generate anchor in format {#manuals:introduction}
                            anchor = "{#" + filename[:-3].replace("/", ":").lstrip(":") + "}"
                            # replace the relative links to anchors in .md files
                            replace_in_file(target_file, r"\((/|https://.{0,4}defold\.com/)?manuals/(.+?)(/)?\)", path_to_manuals_anchor)
                            # convert links to assets and other resources to absolute links
                            replace_in_file(target_file, r"\.\./images/", r"https://defold.com/manuals/images/")
                            replace_in_file(target_file, r"\.\./assets/", r"https://defold.com/manuals/assets/")
                            replace_in_file(target_file, r"\((/ref/|/assets|/tags/|/examples|/why|/product|/faq)", r"(https://defold.com\1")
                            # remove the frontmatter
                            replace_in_file(target_file, r"---\n(.*?)---\n+", r"", re.DOTALL)
                            # put anchor in the first heading of the file
                            replace_in_first_line(target_file, r"^(#+ .+?)$", r"\1 {}".format(anchor), re.MULTILINE)

                    else:
                        update_file_links_with_locale(filename, r'/manuals/[^)#]+', locale)
                        replace_in_file(filename, r"\.\.\/images\/", r"/manuals/images/")
                        replace_in_file(filename, r"\.\.\/assets\/", r"/manuals/assets/")

            print("...faq ({})".format(locale))
            faq_src_dir = os.path.join(DOC_DIR, "docs", locale, "faq")
            if os.path.exists(faq_src_dir):
                faq_dst_dir = get_locale_specific_dir(locale, "faq")
                rmcopytree(faq_src_dir, faq_dst_dir)
                for filename in find_files(faq_dst_dir, "*.md"):
                    process_doc_file(filename, locale)
                    append_frontmatter(filename, {
                        "locale": locale,
                        "layout": "faq",
                    })
                    if locale != "en":
                        update_file_links_with_locale(filename, r'\/manuals\/[^)#]+', locale)
                        replace_in_file(filename, r"\.\.\/images\/", r"/manuals/images/")
                        replace_in_file(filename, r"\.\.\/assets\/", r"/manuals/assets/")

        for locale in locales["languages"].keys():
            print("...shared includes ({})".format(locale))
            shared_includes_src_dir_en = os.path.join(DOC_DIR, "docs", "en", "shared")
            shared_includes_src_dir = os.path.join(DOC_DIR, "docs", locale, "shared")
            shared_includes_dst_dir = os.path.join("_includes", "shared", locale)
            rmcopytree(shared_includes_src_dir_en, shared_includes_dst_dir)
            if os.path.exists(shared_includes_src_dir):
                copytree(shared_includes_src_dir, shared_includes_dst_dir, overwrite = True)
            shutil.rmtree(os.path.join(shared_includes_dst_dir, "images"))
            for filename in find_files(shared_includes_dst_dir, "*.md"):
                process_doc_file(filename, locale)

        for locale in locales["languages"].keys():
            print("...tutorials ({})".format(locale))
            tutorials_src_dir = os.path.join(DOC_DIR, "docs", locale, "tutorials")
            if os.path.exists(tutorials_src_dir):
                tutorials_dst_dir = get_locale_specific_dir(locale, "tutorials")
                rmcopytree(tutorials_src_dir, tutorials_dst_dir)
                for filename in find_files(tutorials_dst_dir, "*.md"):
                    process_doc_file(filename, locale)
                    append_frontmatter(filename, {
                        "locale": locale,
                        "layout": "tutorial",
                    })
                    if locale != "en":
                        update_file_links_with_locale(filename, r'/manuals/[^)#]+', locale)
                        update_file_links_with_locale(filename, r'/tutorials/[^)#]+', locale)
                        replace_in_file(filename, r"\.\.\/images\/", r"/tutorials/images/")

        print("...courses")
        courses_src_dir = os.path.join(DOC_DIR, "docs", "en", "courses")
        courses_dst_dir = "courses"
        rmcopytree(courses_src_dir, courses_dst_dir)
        for filename in find_files(courses_dst_dir, "*.md"):
            process_doc_file(filename, "en")
            append_frontmatter(filename, { "layout": "course" })

        # figure out in which locales each manual exists
        print("...index (incl. locales)")
        for section in index["navigation"]["manuals"]:
            for item in section["items"]:
                item["locales"] = get_index_item_locales(item, locales)
        for item in index["navigation"]["tutorials"]:
            if not item["path"].startswith("http"):
                item["locales"] = get_index_item_locales(item, locales)
        write_as_json(index_file, index)

        print("...shared images")
        shared_images_src_dir = os.path.join(DOC_DIR, "docs", "en", "shared", "images")
        shared_images_dst_dir = os.path.join("shared", "images")
        rmcopytree(shared_images_src_dir, shared_images_dst_dir)

        print("...generating llms/manuals")
        generate_llms_manuals(index)

        print("Done")


def parse_extension_parameters(parameters):
    params = []
    if parameters:
        for p in parameters:
            param = {}
            param_type = p.get("type", "")
            param["name"] = p.get("name", "")
            param["types"] = param_type.split("|") if isinstance(param_type, str) else param_type
            param["doc"] = p.get("desc", "")
            subp = parse_extension_parameters(p.get("parameters")) + parse_extension_parameters(p.get("members")) + parse_extension_parameters(p.get("fields"))
            if subp:
                param["parameters"] = subp
            params.append(param)
    return params

def parse_script_api_members(api_name, api):
    md = create_markdown()
    elements = []
    members = api["members"]
    for m in members:
        element = {}
        element["parameters"] = parse_extension_parameters(m.get("parameters", []))
        element["returnvalues"] = []
        for r in m.get("returns", []):
            ret = {}
            ret["name"] = r.get("type", "")
            ret["doc"] = r.get("desc", "")
            element["returnvalues"].append(ret)
        element["description"] = m.get("desc", "")
        member_name = m.get("name", "")
        member_type = m.get("type", "").upper()
        if member_type == "NUMBER":
            member_type = "VARIABLE"
        element["type"] = member_type
        if member_type == "FUNCTION":
            element["name"] = api_name + "." + member_name
        elif member_type == "TABLE":
            if m.get("members"):
                elements.extend(parse_script_api_members(api_name + "." + member_name, m))
        else:
            element["name"] = m.get("name", "")
        examples = []
        for e in m.get("examples", []):
            desc = e.get("desc", "")
            examples.append(md.convert(desc))
        element["examples"] = "\n".join(examples)
        elements.append(element)
    return elements

def process_extension(extension_name, download = False):
    extension_zip = extension_name + ".zip"
    github_url = "https://github.com/defold/{}".format(extension_name)
    if download:
        if os.path.exists(extension_zip):
            os.remove(extension_zip)

        for branch in ("master", "main"):
            url = github_url + "/archive/" + branch + ".zip"
            if download_file(url, ".", extension_zip):
                break

    if not os.path.exists(extension_zip):
        print("File {} does not exist".format(extension_zip))
        sys.exit(1)

    print("Processing %s" % extension_zip)
    with tmpdir() as tmp_dir:
        shutil.copyfile(extension_zip, os.path.join(tmp_dir, extension_zip))
        unzip(os.path.join(tmp_dir, extension_zip), tmp_dir)
        unzipped_extension_dir = None
        for suffix in ("master", "main"):
            unzipped_extension_dir = os.path.join(tmp_dir, extension_name + "-" + suffix)
            if os.path.exists(unzipped_extension_dir):
                break

        extension_dir = extension_name
        rmmkdir(extension_dir)

        # copy the documentation
        docs_dir = os.path.join(unzipped_extension_dir, "docs")
        rmcopytree(docs_dir, extension_dir)

        index = os.path.join(extension_dir, "index.md")
        for filename in find_files(extension_dir, "*.md"):
            locale = get_doc_locale(os.path.relpath(filename, extension_dir))
            toc = generate_toc(filename)
            append_frontmatter(filename, {
                "layout": "manual",
                "locale": locale,
                "github": "{}".format(github_url),
                "toc": toc,
            })
            process_doc_file(filename, locale)

        for filename in find_files(unzipped_extension_dir, "*.script_api"):

            # create a json data file for the API reference
            # we generate it from the .script_api file (YAML format)
            refdoc = {}
            elements = []
            refdoc["elements"] = elements
            info = {}
            refdoc["info"] = info

            api = yaml.safe_load(read_as_string(filename))[0]
            api_name = api.get("name", "")

            # append links to api reference to the end of the file
            append_to_file(index, "\n## API reference\n[API Reference - {}](/{}/{}_api)\n".format(api_name, extension_dir, api_name))

            info["group"] = "EXTENSIONS"
            info["description"] = api.get("desc", "")
            info["namespace"] = api_name
            info["api_language"] = "Lua"
            info["name"] = extension_name
            info["brief"] = api_name
            info["type"] = "Extension"
            info["api"] = os.path.join(extension_dir, api_name + "_api")
            elements.extend(parse_script_api_members(api_name, api))

            # generate a dummy markdown page with some front matter for the api doc
            api_filename = os.path.join(extension_dir, api_name + "_api.html")
            with open(api_filename, "w") as f:
                fm_branch = "stable"
                fm_ref = info["name"] + "_" + info["namespace"]
                fm_language = info["api_language"]
                fm_title = info["name"]
                fm_type = info["type"]
                f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_language, fm_title, fm_type, "") + REFDOC_MD_BODY)

            # write the json data file
            extension_data_dir = os.path.join("_data", "extensions")
            makedirs(extension_data_dir)
            extension_data_file = os.path.join(extension_data_dir, extension_name + "_" + api_name + ".json")
            write_as_json(extension_data_file, refdoc)


def process_examples(download = False, examples_ref = "master", changed_examples = None):
    examples_sha1 = get_sha1(EXAMPLES_DEFOLD_CHANNEL)

    if download:
        if os.path.exists(EXAMPLES_ZIP):
            os.remove(EXAMPLES_ZIP)
        download_file("https://github.com/defold/examples/archive/{}.zip".format(examples_ref), ".", EXAMPLES_ZIP)
        download_bob(examples_sha1)

    if not os.path.exists(EXAMPLES_ZIP):
        print("File {} does not exist".format(EXAMPLES_ZIP))
        sys.exit(1)

    bob_jar = get_bob_filename(examples_sha1)
    if not os.path.exists(bob_jar):
        print("File {} does not exist".format(bob_jar))
        sys.exit(1)

    rebuild = True

    includes_dir = os.path.join("_includes", "examples")
    rmmkdir(includes_dir)

    print("Processing examples")
    with tmpdir() as tmp_dir:
        shutil.copyfile(EXAMPLES_ZIP, os.path.join(tmp_dir, EXAMPLES_ZIP))
        unzip(os.path.join(tmp_dir, EXAMPLES_ZIP), tmp_dir)
        unzipped_examples_dir = find_unzipped_repo_dir(tmp_dir, "examples-")
        if not unzipped_examples_dir:
            print("Unable to find unzipped examples directory")
            sys.exit(1)

        data_index_file = os.path.join("_data", "examplesindex.json")
        examplesindex = []

        category_dirs = os.listdir(unzipped_examples_dir)
        for category in category_dirs:
            category_src_dir = os.path.join(unzipped_examples_dir, category)
            category_dst_dir = os.path.join("examples", category)
            if os.path.isfile(category_src_dir) or category == ".github":
                continue

            if rebuild:
                rmmkdir(category_dst_dir)

            for example in os.listdir(category_src_dir):
                example_src_dir = os.path.join(category_src_dir, example)
                example_dst_dir = os.path.join(category_dst_dir, example)
                example_path = "%s/%s" % (category, example)

                if os.path.isfile(example_src_dir):
                    continue

                print("..processing %s" % example)
                if rebuild:
                    print("...building %s" % example)
                    bob_out = os.path.join(example_src_dir, bob_jar)
                    shutil.copyfile(bob_jar, bob_out)
                    game_project = os.path.join(example_src_dir, "game.project")
                    replace_in_file(game_project, r"title = .*", r"title = Defold-examples")
                    subprocess.run([ "java", "-jar", bob_out, "--archive", "--platform", "wasm-web", "--architectures", "wasm-web", "--variant", "debug", "--build-server", EXAMPLES_BUILD_SERVER, "resolve", "build", "bundle" ], cwd=example_src_dir, check=True)
                    os.remove(bob_out)

                    print("...copying %s" % example)
                    bundle_index_file = find_file(os.path.join(example_src_dir, "build", "default"), "index.html")
                    if not bundle_index_file:
                        print("File index.html not found")
                        sys.exit(1)
                    print(bundle_index_file, os.path.dirname(bundle_index_file))

                    bundle_dir = os.path.dirname(bundle_index_file)
                    rmtree(example_dst_dir)
                    makedirs(category_dst_dir)
                    shutil.copytree(bundle_dir, example_dst_dir)
                    os.remove(os.path.join(example_dst_dir, "index.html"))
                else:
                    os.makedirs(example_dst_dir, exist_ok=True)

                print("...parsing example.md")
                md_file = os.path.join(example_src_dir, "example.md")
                fm = load_frontmatter(md_file)
                fm["category"] = category
                fm["path"] = example_path
                fm["layout"] = "example"
                if "thumbnail" in fm:
                    image_path = "https://www.defold.com/examples/%s/%s" % (fm["path"], fm["thumbnail"])
                    fm["opengraph_image"] = image_path
                    fm["twitter_image"] = image_path
                else:
                    # Try to find the first image in the markdown content
                    content = read_as_string(md_file)
                    # Look for markdown image syntax: ![alt](image.ext)
                    image_match = re.search(r'!\[.*?\]\(([^)]+\.(png|jpg|jpeg|gif|webp))\)', content)
                    if image_match:
                        first_image = image_match.group(1)
                        # Check if image exists in the example directory
                        if os.path.exists(os.path.join(example_src_dir, first_image)):
                            fm["thumbnail"] = first_image
                            image_path = "https://www.defold.com/examples/%s/%s" % (fm["path"], first_image)
                            fm["opengraph_image"] = image_path
                            fm["twitter_image"] = image_path

                print("...copying example scripts")
                os.makedirs(os.path.join(includes_dir, category, example), exist_ok=True)
                copied_scripts = set()
                for script in find_files(os.path.join(example_src_dir, "example"), EXAMPLE_CODE_FILE_PATTERNS):
                    include_name = example_include_name(script)
                    copied_scripts.add(include_name)
                    tgt = os.path.join(includes_dir, category, example, include_name)
                    shutil.copyfile(script, tgt)

                frontmatter_scripts = split_example_scripts(fm.get("scripts"))
                if frontmatter_scripts:
                    missing_scripts = []
                    for script in frontmatter_scripts:
                        if script != os.path.basename(script) or example_include_name(script) not in copied_scripts:
                            missing_scripts.append(script)
                    if missing_scripts:
                        print("ERROR: {} references missing example script(s): {}".format(fm["path"], ", ".join(missing_scripts)))
                        sys.exit(1)

                examplesindex.append(fm)
                replace_frontmatter(md_file, fm)

                print("...copying example.md")
                shutil.copyfile(md_file, os.path.join(example_dst_dir, "index.md"))

                print("...copying images")
                for image in find_files(example_src_dir, "*.png|*.jpg|*.gif|*.webp|*.webm"):
                    tgt = os.path.join(example_dst_dir, os.path.basename(image))
                    shutil.copyfile(image, tgt)

        print("...generating index")
        if os.path.exists(data_index_file):
            os.remove(data_index_file)
        examplesindex.sort(key=lambda x: x.get("path").lower())
        write_as_json(data_index_file, examplesindex)

        print("...generating llms/examples")
        generate_llms_examples()

        print("...deduplicating wasm artifacts")
        dedupe_examples_wasm.run()


def process_codepad(download = False):
    if download:
        if os.path.exists(CODEPAD_ZIP):
            os.remove(CODEPAD_ZIP)
        download_file("https://github.com/defold/codepad/archive/master.zip", ".", CODEPAD_ZIP)
        download_bob(get_sha1())

    if not os.path.exists(CODEPAD_ZIP):
        print("File {} does not exist".format(CODEPAD_ZIP))
        sys.exit(1)

    bob_jar = get_bob_filename(get_sha1())
    if not os.path.exists(bob_jar):
        print("File {} does not exist".format(bob_jar))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(CODEPAD_ZIP, os.path.join(tmp_dir, CODEPAD_ZIP))
        unzip(os.path.join(tmp_dir, CODEPAD_ZIP), tmp_dir)

        shutil.copyfile(bob_jar, os.path.join(tmp_dir, bob_jar))

        input_dir = os.path.join(tmp_dir, "codepad-master")
        subprocess.call([ "java", "-jar", os.path.join(tmp_dir, bob_jar),
            "--archive",
            "--platform", "wasm-web",
            "--architectures", "wasm-web",
            "--variant", "debug",
            "resolve", "distclean", "build", "bundle"
        ], cwd=input_dir)

        codepad_dir = "codepad"
        rmcopytree(os.path.join(input_dir, "build", "default", "DefoldCodePad"), codepad_dir)


ASSET_ALLOWED_TAG_NAMES = None

def normalize_asset_tag_id(tag):
    return re.sub(r"[^a-z0-9]+", "", (tag or "").lower())

def get_asset_allowed_tag_names():
    global ASSET_ALLOWED_TAG_NAMES
    if ASSET_ALLOWED_TAG_NAMES is None:
        with open("_config.yml") as f:
            config = yaml.safe_load(f) or {}
        tags = config.get("asset_allowed_tags", [])
        ASSET_ALLOWED_TAG_NAMES = {}
        for tag in tags:
            tag_name = tag.get("name") if isinstance(tag, dict) else str(tag)
            tag_id = tag.get("id") if isinstance(tag, dict) else normalize_asset_tag_id(tag_name)
            ASSET_ALLOWED_TAG_NAMES[normalize_asset_tag_id(tag_id)] = tag_name
            ASSET_ALLOWED_TAG_NAMES[normalize_asset_tag_id(tag_name)] = tag_name
    return ASSET_ALLOWED_TAG_NAMES

def fix_tags_case(tags, asset_id=None):
    if tags:
        allowed_tags = get_asset_allowed_tag_names()
        normalized_tags = []
        seen = set()
        for tag in tags:
            tag_id = normalize_asset_tag_id(tag)
            if tag_id not in allowed_tags:
                asset_label = " in {}".format(asset_id) if asset_id else ""
                raise ValueError("Unknown asset tag{}: {}".format(asset_label, tag))

            normalized_tag = allowed_tags[tag_id]
            normalized_tag_id = normalize_asset_tag_id(normalized_tag)
            if normalized_tag_id and normalized_tag_id not in seen:
                normalized_tags.append(normalized_tag)
                seen.add(normalized_tag_id)
        tags[:] = normalized_tags
    return tags

def validate_asset_tags(asset_source_dir):
    allowed_tags = get_asset_allowed_tag_names()
    unknown_tags = []
    for filename in find_files(asset_source_dir, "*.json"):
        asset_id = os.path.basename(filename).replace(".json", "")
        asset = read_as_json(filename)
        for tag in asset.get("tags", []):
            if normalize_asset_tag_id(tag) not in allowed_tags:
                unknown_tags.append("{}: {}".format(asset_id, tag))

    if unknown_tags:
        details = "\n".join(unknown_tags[:50])
        if len(unknown_tags) > 50:
            details += "\n... and {} more".format(len(unknown_tags) - 50)
        raise ValueError("Unknown asset tags:\n{}".format(details))

def fix_platforms_case(platforms):
    if platforms:
        if platforms[0].lower() == "*":
            platforms.clear()
            platforms.extend(["ios", "android", "html5", "windows", "linux", "macos"])

        for i,platform in enumerate(platforms):
            if platform.lower() == "ios":
                platforms[i] = "iOS"
            elif platform.lower() == "html5":
                platforms[i] = "HTML5"
            elif platform.lower() == "macos":
                platforms[i] = "macOS"
            else:
                platforms[i] = platform.capitalize()
    return platforms

def process_assets(tmp_dir):
    asset_source_dir = os.path.join(tmp_dir, "asset-portal-master", "assets")
    validate_asset_tags(asset_source_dir)

    # Jekyll assets collection
    asset_collection_dir = "assets"
    rmmkdir(asset_collection_dir)

    # Jekyll authors collection
    author_collection_dir = "authors"
    rmmkdir(author_collection_dir)

    # Jekyll asset data
    asset_data_dir = os.path.join("_data", "assets")
    rmmkdir(asset_data_dir)

    # Jekyll author data
    author_data_dir = os.path.join("_data", "authors")
    rmmkdir(author_data_dir)

    # Jekyll tag data
    tag_data_dir = os.path.join("_data", "tags")
    rmmkdir(tag_data_dir)

    # image data
    image_dir = os.path.join("images", "assets")
    rmcopytree(os.path.join(asset_source_dir, "images"), image_dir)

    assetindex = []
    authorindex = {}
    tagindex = {}
    platformindex = {}
    for filename in find_files(asset_source_dir, "*.json"):
        basename = os.path.basename(filename)
        print("Processing asset: {}".format(basename))
        asset_id = basename.replace(".json", "")

        # copy the data file as-is
        asset_file = os.path.join(asset_data_dir, basename)
        shutil.copyfile(filename, asset_file)

        # read asset and add additional data
        asset = read_as_json(asset_file)
        fix_tags_case(asset["tags"], asset_id)
        fix_platforms_case(asset["platforms"])
        author_name = asset["author"]
        project_url = asset.get("project_url") or asset.get("github_url") or ""

        author_id = hashlib.md5(author_name.encode('utf-8')).hexdigest()
        asset["author_id"] = author_id
        asset["asset_url"] = "https://github.com/defold/asset-portal/blob/master/assets/%s.json" % asset_id
        asset["project_url"] = project_url
        asset.pop("github_url", None)
        asset.pop("latest_release_url", None)
        write_as_json(asset_file, asset, False)

        # build asset index
        assetindex.append({
            "id": asset_id,
            "tags": asset["tags"],
            "platforms": asset["platforms"],
            "stars": asset.get("stars") or 0,
            "timestamp": asset.get("timestamp") or 0
        })

        # build tag index
        for tag in asset["tags"]:
            if not tag in tagindex:
                tagindex[tag] = {
                    "id": tag.lower().replace(" ", ""),
                    "name": tag,
                    "assets": []
                }
            tagindex[tag]["assets"].append({
                "id": asset_id,
                "stars": asset.get("stars") or 0,
                "timestamp": asset.get("timestamp") or 0
            })
            tagindex[tag]["assets"].sort(key=lambda x: x.get("id").lower())

        # build platform index
        for platform in asset["platforms"]:
            if not platform in platformindex:
                platformindex[platform] = {
                    "id": platform.lower().replace(" ", ""),
                    "name": platform,
                    "assets": []
                }
            platformindex[platform]["assets"].append({
                "id": asset_id,
                "stars": asset.get("stars") or 0
            })
            platformindex[platform]["assets"].sort(key=lambda x: x.get("id").lower())

        # build author index
        if not author_id in authorindex:
            authorindex[author_id] = {
                "id": author_id,
                "name": author_name,
                "assets": []
            }
        authorindex[author_id]["assets"].append({
            "id": asset_id,
            "stars": asset.get("stars") or 0
        })
        authorindex[author_id]["assets"].sort(key=lambda x: x.get("id").lower())

        # generate a dummy markdown page with some front matter for each asset
        with open(os.path.join(asset_collection_dir, basename.replace(".json", ".md")), "w") as f:
            asset_name = asset["name"]
            asset_desc = asset["description"].strip()
            asset_image = asset.get("images", {}).get("thumb", None)
            if asset_image and not asset_image.startswith("http"):
                asset_image = "https://www.defold.com/images/assets/" + asset_image
            else:
                asset_image = "https://www.defold.com/images/asset-nohero.jpg"
            f.write(ASSET_MD_FRONTMATTER.format(asset_id, asset_name, asset_desc, asset_image, asset_image))

    # write asset index
    assetindex.sort(key=lambda x: x.get("id").lower())
    write_as_json(ASSETINDEX_JSON, assetindex, False)

    # write author index
    authorlist = authorindex.values()
    authorlist = sorted(authorlist, key=lambda x: x.get("name").lower())
    write_as_json(AUTHORINDEX_JSON, authorlist, False)

    # write author data and a dummy markdown page with front matter
    for author in authorlist:
        author["assets"].sort(key=lambda x: x.get("id"))
        filename = os.path.join(author_data_dir, author["id"] + ".json")
        write_as_json(filename, author, False)
        with open(os.path.join(author_collection_dir, author["id"] + ".md"), "w") as f:
            f.write(AUTHOR_MD_FRONTMATTER.format(author["id"], author["name"]))

    # write tag index
    taglist = tagindex.values()
    taglist = sorted(taglist, key=lambda x: x.get("id").lower())
    write_as_json(TAGINDEX_JSON, taglist, False)

    # write platform index
    # platformlist = platformindex.values()
    # platformlist.sort(key=lambda x: x.get("id").lower())
    # write_as_json(PLATFORMINDEX_JSON, platformlist)

    # Jekyll tags collection (one subdirectory per sort order)
    tag_collection_dir = "tags"
    sort_orders = ["stars", "timestamp"]
    for sort_order in sort_orders:
        rmmkdir(os.path.join(tag_collection_dir, sort_order))

    # write tag data
    for tag in taglist:
        tag["assets"].sort(key=lambda x: x.get("id"))

        # _data/tags
        filename = os.path.join(tag_data_dir, tag["id"] + ".json")
        with open(filename, "w") as f:
            f.write(json.dumps(tag, indent=2, sort_keys=True, ensure_ascii=False))

        # tags/stars, tags/timestamp
        for sort_order in sort_orders:
            with open(os.path.join(tag_collection_dir, sort_order, tag["id"] + ".md"), "w") as f:
                f.write(TAG_SORT_MD_FRONTMATTER.format(tag["id"], tag["name"], sort_order))

def process_games(tmp_dir):
    # image data
    image_dir = os.path.join("images", "games")
    rmcopytree(os.path.join(tmp_dir, "games-showcase-master", "games", "images"), image_dir)

    # update existing games with new info (except show+placement)
    # maintain existing order
    # add new games last
    games = read_as_json(GAMES_JSON)

    # Track the IDs that exist upstream to allow removal of deleted games
    new_game_ids = set()

    # read new games
    for filename in find_files(os.path.join(tmp_dir, "games-showcase-master", "games"), "*.json"):
        basename = os.path.basename(filename)
        print("Processing game: {}".format(basename))

        # read new game and add additional data
        game_id = basename.replace(".json", "")
        new_game_ids.add(game_id)
        new_game = read_as_json(filename)
        new_game["id"] = game_id

        # try to find game in existing list of games
        found = False
        for game in games:
            if game.get("id") == new_game.get("id"):
                found = True
                # copy data from new game
                # we do this to maintain the order of games in games.json
                for k,v in new_game.items():
                    game[k] = v
        # append new games last
        if not found:
            new_game["games"] = "half"
            games.append(new_game)

    # Remove games that no longer exist in the games-showcase repository
    if new_game_ids:
        games = [g for g in games if g.get("id") in new_game_ids]

    write_as_json(GAMES_JSON, games)


def process_asset_portal(download = False):
    if download:
        if os.path.exists(ASSETPORTAL_ZIP):
            os.remove(ASSETPORTAL_ZIP)
        download_file("https://github.com/defold/asset-portal/archive/master.zip", ".", ASSETPORTAL_ZIP)

    if not os.path.exists(ASSETPORTAL_ZIP):
        print("File {} does not exist".format(ASSETPORTAL_ZIP))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(ASSETPORTAL_ZIP, os.path.join(tmp_dir, ASSETPORTAL_ZIP))
        unzip(os.path.join(tmp_dir, ASSETPORTAL_ZIP), tmp_dir)
        process_assets(tmp_dir)

def process_games_showcase(download = False):
    if download:
        if os.path.exists(GAMESSHOWCASE_ZIP):
            os.remove(GAMESSHOWCASE_ZIP)
        download_file("https://github.com/defold/games-showcase/archive/master.zip", ".", GAMESSHOWCASE_ZIP)

    if not os.path.exists(GAMESSHOWCASE_ZIP):
        print("File {} does not exist".format(GAMESSHOWCASE_ZIP))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(GAMESSHOWCASE_ZIP, os.path.join(tmp_dir, GAMESSHOWCASE_ZIP))
        unzip(os.path.join(tmp_dir, GAMESSHOWCASE_ZIP), tmp_dir)
        process_games(tmp_dir)



def process_refdoc(download = False):
    refindex = []
    branchindex = [ "alpha", "beta", "stable" ]
    ref_root_dir = "ref"
    rmmkdir(ref_root_dir)

    for branch in branchindex:
        print("Processing branch", branch)
        REFDOC_ZIP = "refdoc_{}.zip".format(branch)
        REF_DATA_DIR = os.path.join("_data", "ref", branch)
        REF_PAGE_DIR = os.path.join(ref_root_dir, branch)

        if download:
            if os.path.exists(REFDOC_ZIP):
                os.remove(REFDOC_ZIP)
            download_file("http://d.defold.com/archive/{}/engine/share/ref-doc.zip".format(get_sha1(branch)), ".", REFDOC_ZIP)

        if not os.path.exists(REFDOC_ZIP):
            print("File {} does not exist".format(REFDOC_ZIP))
            sys.exit(1)

        with tmpdir() as tmp_dir:
            shutil.copyfile(REFDOC_ZIP, os.path.join(tmp_dir, REFDOC_ZIP))
            unzip(os.path.join(tmp_dir, REFDOC_ZIP), tmp_dir)

            # Jekyll page and data dir
            rmmkdir(REF_PAGE_DIR)
            rmmkdir(REF_DATA_DIR)

            # multiple files can contribute to the same namespace
            # find and merge apis per namespace
            namespaces = {}
            files = list_files(os.path.join(tmp_dir, "doc"), ".json", sort = True)
            for file in files:
                api = read_as_json(os.path.join(tmp_dir, "doc", file))
                # ignore empty APIs (such as those moved to extensions)
                if len(api["elements"]) > 0:
                    namespace = api["info"]["namespace"]
                    if not namespace:
                        print("WARNING! No namespace found in %s. Using name instead" % file)
                        namespace = api["info"]["name"].replace(" ", "")
                    if not namespace:
                        print("WARNING! No namespace or name found in %s. Using filename" % file)
                        namespace = file
                    api["info"]["namespace"] = namespace

                    # detect API language with fallback
                    api_language = get_api_language(api["info"], default=None)
                    if not api_language:
                        if namespace.startswith("dm"):
                            print("  No API language found in %s, inferring C++ from namespace" % file)
                            api_language = "C++"
                        elif "script_" in api["info"]["path"]:
                            print("  No API language found in %s, inferring Lua from path" % file)
                            api_language = "Lua"
                        else:
                            print("  No API language found in %s, assuming Lua" % file)
                            api_language = "Lua"
                    api["info"]["api_language"] = api_language

                    # set api type
                    api["info"]["type"] = "Defold " + api_language

                    # make sure file is only the filename and no path
                    if api["info"]["file"] == "":
                        api["info"]["file"] = os.path.basename(api["info"]["path"])
                    elif str.find(api["info"]["file"], "/") != -1:
                        api["info"]["file"] = os.path.basename(api["info"]["file"])

                    # generate include path for C/C++ files
                    if api_language in ("C++", "C"):
                        dmsdk_index = str.find(api["info"]["path"], "dmsdk/")
                        api["info"]["include"] = api["info"]["path"]
                        if dmsdk_index != -1:
                            api["info"]["include"] = api["info"]["path"][dmsdk_index:]

                    # create the key by which we index and collect APIs
                    namespace_key = namespace
                    if api_language == "C++":
                        # namespace_key = namespace_key + "-cpp"
                        namespace_key = api["info"]["path"].replace("..", "").replace("/", "-").replace(".", "-")
                    elif api_language == "C#":
                        # namespace_key = namespace_key + "-cs"
                        namespace_key = api["info"]["path"].replace("..", "").replace("/", "-").replace(".", "-")
                    else:
                        namespace_key = namespace_key + "-" + api_language
                    namespace_key = namespace_key.lower()

                    # add api or extend existing one
                    if not namespace_key in namespaces:
                        namespaces[namespace_key] = api
                    else:
                        # extend info
                        info = namespaces[namespace_key]["info"]
                        if not info["namespace"]: info["namespace"] = api["info"]["namespace"]
                        if not info["description"]: info["description"] = api["info"]["description"]
                        if not info["brief"]: info["brief"] = api["info"]["brief"]
                        if not info["path"]: info["path"] = api["info"]["path"]
                        if not info["file"]: info["file"] = api["info"]["file"]
                        info["notes"].extend(api["info"]["notes"])
                        # extend elements
                        elements = namespaces[namespace_key]["elements"]
                        elements.extend(api["elements"])

            # do per namespace processing and generate index and dummy file per namespace
            md = create_markdown()
            for namespace_key in namespaces:
                api = namespaces[namespace_key]

                # create html version of description
                api["info"]["description_html"] = md.convert(api["info"]["description"])

                api["elements"].sort(key=lambda x: x.get("name").lower())

                json_out_name = namespace_key
                json_out_file = json_out_name + ".json"
                
                # write the json data file for the api
                # example: _data/ref/stable/go.json
                p = os.path.join(REF_DATA_DIR, json_out_file)
                print("  " + json_out_name + " path: " + p + " api_language: " + api["info"].get("api_language"))
                write_as_json(p, api)

                # generate a dummy markdown page with some front matter for each ref doc
                # example: ref/stable/go-lua.md, ref/stable/dmarray-cpp.md etc
                dummy = os.path.join(REF_PAGE_DIR, json_out_name + ".md")
                with open(dummy, "w") as f:
                    fm_branch = branch
                    fm_ref = json_out_name
                    fm_language = api["info"]["api_language"]
                    fm_title = api["info"]["name"]
                    fm_type = api["info"]["type"]
                    f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_language, fm_title, fm_type, "") + REFDOC_MD_BODY)

                # for backwards compatibility also generate one using only the namespace
                # example: ref/stable/go.md, ref/stable/dmarray.md etc
                json_out_name_fallback = api["info"]["namespace"].lower()
                dummy = os.path.join(REF_PAGE_DIR, json_out_name_fallback + ".md")
                with open(os.path.join(REF_PAGE_DIR, json_out_name_fallback + ".md"), "w") as f:
                    fm_branch = branch
                    fm_ref = json_out_name
                    fm_language = api["info"]["api_language"]
                    fm_title = api["info"]["name"]
                    fm_type = api["info"]["type"]
                    f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_language, fm_title, fm_type, "pagefind_exclude: true\n") + REFDOC_MD_BODY)

                # build refdoc index
                refindex.append({
                    "namespace": api["info"]["namespace"],
                    "file": api["info"]["file"],
                    "path": api["info"]["path"],
                    "name": api["info"]["name"],
                    "filename": json_out_name,
                    "url": "/ref/" + branch + "/" + json_out_name,
                    "branch": branch,
                    "api_language": api["info"]["api_language"],
                    "type": api["info"]["type"],
                })

        # add extensions
        extensions_data_dir = os.path.join("_data", "extensions")
        for filename in os.listdir(extensions_data_dir):
            extension = read_as_json(os.path.join(extensions_data_dir, filename))
            extension_api_language = get_api_language(extension["info"], default="Lua")
            refindex.append({
                "namespace": extension["info"]["namespace"],
                "name": extension["info"]["name"],
                "filename": extension["info"]["name"] + "_" + extension["info"]["namespace"],
                "url": "/" + extension["info"]["api"],
                "branch": branch,
                "api_language": extension_api_language,
                "type": extension["info"]["type"],
            })

        # generate a list of API types
        types = []
        typerefs = []
        for ref in refindex:
            if ref["type"] not in types:
                types.append(ref["type"])
                typerefs.append(ref)

        # write overview pages
        for typeref in typerefs:
            type = typeref["type"]
            filename = "overview_" + type.replace(" ", "").replace("C++", "cpp").lower() + ".md"
            print("  " + filename, branch)
            with open(os.path.join(REF_PAGE_DIR, filename), "w") as f:
                fm_branch = branch
                fm_ref = "overview"
                fm_language = typeref["api_language"]
                fm_title = "Overview"
                fm_type = type
                f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_language, fm_title, fm_type, "") + REFDOC_MD_BODY)


    # copy stable files to ref/ for backwards compatibility
    for item in os.listdir(os.path.join("ref", "stable")):
        s = os.path.join("ref", "stable", item)
        d = os.path.join("ref", item)
        if not os.path.isdir(s):
            shutil.copy2(s, d)

    refindex.sort(key=lambda x: x.get("name").lower() + x.get("branch").lower())

    # write refdoc index
    write_as_json(os.path.join("_data", "refindex.json"), refindex)

    # write branch index
    write_as_json(os.path.join("_data", "branchindex.json"), branchindex)

    print("...generating llms/apis")
    generate_llms_apis()


def commit_changes():
    call("git config user.name 'github-actions[bot]'")
    call("git config user.email '41898282+github-actions[bot]@users.noreply.github.com'")
    call("git add -A")
    if subprocess.call([ "git", "diff", "--cached", "--quiet" ]) == 0:
        print("No changes to commit")
        return

    subprocess.run([ "git", "commit", "-m", "Site changes" ], check=True)
    for attempt in range(1, 4):
        print("Pushing generated changes (attempt {})".format(attempt))
        try:
            subprocess.run([ "git", "fetch", "origin", "master" ], check=True)
            subprocess.run([ "git", "rebase", "origin/master" ], check=True)
            subprocess.run([ "git", "push", "origin", "HEAD:master" ], check=True)
            return
        except subprocess.CalledProcessError:
            subprocess.call([ "git", "rebase", "--abort" ])
            if attempt == 3:
                raise
            subprocess.run([ "git", "fetch", "origin", "master" ], check=True)


ALL_COMMANDS = [ "all", "help", "docs", "refdoc", "asset-portal", "games-showcase", "examples", "codepad", "commit", "extensions" ]
ALL_COMMANDS.sort()

parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (' + ', '.join(ALL_COMMANDS) + ')')
parser.add_argument("--extension", dest="extensions", action='append', help="Which extension to process")
parser.add_argument("--download", dest="download", action='store_true', help="Download updated content for the command(s) in question")
parser.add_argument("--examples-ref", dest="examples_ref", default="master", help="Git ref to import from defold/examples")
parser.add_argument("--changed-examples", dest="changed_examples", default="", help="Comma or whitespace separated example paths to import incrementally")
parser.add_argument("--changed-examples-json", dest="changed_examples_json", default="", help="JSON array of example paths to import incrementally")
args = parser.parse_args()

help = """
COMMANDS:
docs = Process the docs (manuals, tutorials and faq)
refdoc = Process the API reference
asset-portal = Process the assets list (from asset-portal)
games-showcase = Process the games list (from games-showcase)
examples = Build the examples
codepad = Build the Defold CodePad
commit = Commit changed files
extensions = Process the docs for official extensions (use --extension to specify which extensions to process)
all = Run all of the above commands
help = Show this help
"""

if "all" in args.commands:
    commands = []
    commands.extend(ALL_COMMANDS)
    commands.remove("all")
    commands.remove("help")
    # make sure commit is the last command
    commands.remove("commit")
    commands.append("commit")
    args.commands = commands

for command in args.commands:
    if command == "help":
        parser.print_help()
        print(help)
        sys.exit(0)
    elif command == "docs":
        process_docs(download = args.download)
    elif command == "extensions":
        for extension in args.extensions:
            process_extension(extension, download = args.download)
    elif command == "examples":
        changed_examples = parse_changed_examples(args.changed_examples)
        changed_examples.extend(parse_changed_examples_json(args.changed_examples_json))
        process_examples(download = args.download, examples_ref = args.examples_ref, changed_examples = changed_examples)
    elif command == "refdoc":
        process_refdoc(download = args.download)
    elif command == "asset-portal":
        process_asset_portal(download = args.download)
    elif command == "games-showcase":
        process_games_showcase(download = args.download)
    elif command == "codepad":
        process_codepad(download = args.download)
    elif command == "commit":
        commit_changes()
    else:
        print("Unknown command {}".format(command))
