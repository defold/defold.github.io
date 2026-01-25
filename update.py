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

from markdown import Markdown
from markdown import Extension
from markdown.util import AtomicString
import xml.etree.ElementTree as etree
from markdown.inlinepatterns import Pattern


SHA1 = {}

DOCS_ZIP = "doc-master.zip"
EXAMPLES_ZIP = "examples-master.zip"
CODEPAD_ZIP = "codepad-master.zip"
ASSETPORTAL_ZIP = "asset-portal-master.zip"
GAMESSHOWCASE_ZIP = "games-showcase-master.zip"

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
language: {}
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


def github_request(url, token):
    try:
        response = requests.get(url, headers={"Authorization": "token %s" % (token)})
        response.raise_for_status()
        return response.json()
    except Exception as err:
        print(err)


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


def process_doc_file(file, language):
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
    replace_in_file(file, r"\{\% include shared\/(.*?)\.md(.*?)\%\}", r"{}".format("{% include shared/" + language + "/\\1.md\\2%}"))

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


def get_language_specific_dir(language, dir):
    if language != "en":
        dir = os.path.join(language, dir)
    return dir

def update_file_links_with_lang(filename, pattern, language):
    # Open the file and read its content
    with open(filename, 'r') as f:
        content = f.read()
    
    def is_valid_path_and_lang(path, language):
        # Normalize the path to ensure it doesn't end with a slash
        normalized_path = path.rstrip('/').lstrip('/')
        if os.path.exists(os.path.join(language, normalized_path + ".md")) or os.path.exists(os.path.join(language, normalized_path)):
            return True
        return False

    
    # Use regex to find all patterns and update them if valid
    def replacement(match):
        path = match.group(0)
        # Check if the path exists and has the specified language
        if is_valid_path_and_lang(path, language):
            return '/{}/{}'.format(language, path.lstrip('/'))
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

        print("...languages")
        languages = read_as_json(os.path.join(DOC_DIR, "docs", "languages.json"))
        language_list = []
        for language in languages["languages"].keys():
            language_data = languages["languages"][language]
            if language_data["active"]:
                language_data["language"] = language
                if language == "en":
                    language_data["urlprefix"] = ""
                else:
                    language_data["urlprefix"] = language
                language_list.append(language_data)
        write_as_json(os.path.join("_data", "languageindex.json"), language_list)

        print("...index")
        index_file = os.path.join("_data", "learnindex.json")
        if os.path.exists(index_file):
            os.remove(index_file)
        shutil.copyfile(os.path.join(DOC_DIR, "docs", "en", "en.json"), index_file)
        index = read_as_json(index_file)

        for language in languages["languages"].keys():
            print("...manuals ({})".format(language))
            manuals_src_dir = os.path.join(DOC_DIR, "docs", language, "manuals")
            if os.path.exists(manuals_src_dir):
                manuals_dst_dir = get_language_specific_dir(language, "manuals")
                rmcopytree(manuals_src_dir, manuals_dst_dir)
                for filename in find_files(manuals_dst_dir, "*.md"):
                    process_doc_file(filename, language)
                    # update front matter
                    toc = generate_toc(filename)
                    append_frontmatter(filename, {
                        "layout": "manual",
                        "language": language,
                        "github": "https://github.com/defold/doc",
                        "toc": toc,
                    })
                    if language == "en":
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
                        # replace_in_file(filename, r"\/manuals\/", r"/{}/manuals/".format(language))
                        update_file_links_with_lang(filename, r'/manuals/[^)#]+', language)
                        replace_in_file(filename, r"\.\.\/images\/", r"/manuals/images/".format(language))
                        replace_in_file(filename, r"\.\.\/assets\/", r"/manuals/assets/".format(language))

            print("...faq ({})".format(language))
            faq_src_dir = os.path.join(DOC_DIR, "docs", language, "faq")
            if os.path.exists(faq_src_dir):
                faq_dst_dir = get_language_specific_dir(language, "faq")
                rmcopytree(faq_src_dir, faq_dst_dir)
                for filename in find_files(faq_dst_dir, "*.md"):
                    process_doc_file(filename, language)
                    append_frontmatter(filename, {
                        "language": language,
                        "layout": "faq",
                    })
                    if language != "en":
                        # replace_in_file(filename, r"\/manuals\/", r"/{}/manuals/".format(language))
                        update_file_links_with_lang(filename, r'\/manuals\/[^)#]+', language)
                        replace_in_file(filename, r"\.\.\/images\/", r"/manuals/images/".format(language))
                        replace_in_file(filename, r"\.\.\/assets\/", r"/manuals/assets/".format(language))

        for language in languages["languages"].keys():
            print("...shared includes ({})".format(language))
            shared_includes_src_dir_en = os.path.join(DOC_DIR, "docs", "en", "shared")
            shared_includes_src_dir = os.path.join(DOC_DIR, "docs", language, "shared")
            shared_includes_dst_dir = os.path.join("_includes", "shared", language)
            rmcopytree(shared_includes_src_dir_en, shared_includes_dst_dir)
            if os.path.exists(shared_includes_src_dir):
                copytree(shared_includes_src_dir, shared_includes_dst_dir, overwrite = True)
            shutil.rmtree(os.path.join(shared_includes_dst_dir, "images"))
            for filename in find_files(shared_includes_dst_dir, "*.md"):
                process_doc_file(filename, language)

        print("...tutorials")
        tutorials_src_dir = os.path.join(DOC_DIR, "docs", "en", "tutorials")
        tutorials_dst_dir = "tutorials"
        rmcopytree(tutorials_src_dir, tutorials_dst_dir)
        for filename in find_files(tutorials_dst_dir, "*.md"):
            process_doc_file(filename, "en")
            append_frontmatter(filename, { "layout": "tutorial" })

        print("...courses")
        courses_src_dir = os.path.join(DOC_DIR, "docs", "en", "courses")
        courses_dst_dir = "courses"
        rmcopytree(courses_src_dir, courses_dst_dir)
        for filename in find_files(courses_dst_dir, "*.md"):
            process_doc_file(filename, "en")
            append_frontmatter(filename, { "layout": "course" })

        # figure out in which languages each manual exists
        print("...index (incl. languages)")
        for section in index["navigation"]["manuals"]:
            for item in section["items"]:
                item["languages"] = []
                if not item["path"].startswith("http"):
                    path = item["path"][1:]
                    # foo/bar/#anchor -> foo/bar
                    # foo/bar#anchor -> foo/bar
                    path = re.sub(r"/?\#.*", "", path)
                    for language in languages["languages"].keys():
                        if os.path.exists(get_language_specific_dir(language, path + ".md")):
                            item["languages"].append(language)
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
    md = Markdown(extensions=['markdown.extensions.fenced_code','markdown.extensions.def_list', 'markdown.extensions.codehilite','markdown.extensions.tables'])
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
            toc = generate_toc(filename)
            append_frontmatter(filename, {
                "layout": "manual",
                "language": "en",
                "github": "{}".format(github_url),
                "toc": toc,
            })
            process_doc_file(filename, "en")

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
            info["language"] = "Lua"
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
                fm_language = info["language"]
                fm_title = info["name"]
                fm_type = info["type"]
                f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_language, fm_title, fm_type, "") + REFDOC_MD_BODY)

            # write the json data file
            extension_data_dir = os.path.join("_data", "extensions")
            makedirs(extension_data_dir)
            extension_data_file = os.path.join(extension_data_dir, extension_name + "_" + api_name + ".json")
            write_as_json(extension_data_file, refdoc)


def process_examples(download = False):
    if download:
        if os.path.exists(EXAMPLES_ZIP):
            os.remove(EXAMPLES_ZIP)
        download_file("https://github.com/defold/examples/archive/refs/heads/master.zip", ".", EXAMPLES_ZIP)
        download_bob(get_sha1())

    if not os.path.exists(EXAMPLES_ZIP):
        print("File {} does not exist".format(EXAMPLES_ZIP))
        sys.exit(1)

    bob_jar = get_bob_filename(get_sha1())
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
        unzipped_examples_dir = os.path.join(tmp_dir, "examples-master")

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

                if os.path.isfile(example_src_dir):
                    continue

                print("..processing %s" % example)
                if rebuild:
                    print("...building %s" % example)
                    bob_out = os.path.join(example_src_dir, bob_jar)
                    shutil.copyfile(bob_jar, bob_out)
                    game_project = os.path.join(example_src_dir, "game.project")
                    replace_in_file(game_project, r"title = .*", r"title = Defold-examples")
                    subprocess.call([ "java", "-jar", bob_out, "--archive", "--platform", "js-web", "--architectures", "wasm-web", "--variant", "debug", "resolve", "build", "bundle" ], cwd=example_src_dir)
                    os.remove(bob_out)

                    print("...copying %s" % example)
                    index_file = find_file(os.path.join(example_src_dir, "build", "default"), "index.html")
                    print(index_file, os.path.dirname(index_file))
                    if not index_file:
                        print("File index.html not found")
                        sys.exit(1)

                    bundle_dir = os.path.dirname(index_file)
                    shutil.copytree(bundle_dir, example_dst_dir)
                    os.remove(os.path.join(example_dst_dir, "index.html"))
                else:
                    os.makedirs(example_dst_dir, exist_ok=True)

                print("...parsing example.md")
                md_file = os.path.join(example_src_dir, "example.md")
                fm = load_frontmatter(md_file)
                fm["category"] = category
                fm["path"] = "%s/%s" % (category, example)
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
                examplesindex.append(fm)
                replace_frontmatter(md_file, fm)

                print("...copying example.md")
                shutil.copyfile(md_file, os.path.join(example_dst_dir, "index.md"))

                print("...copying example scripts")
                os.makedirs(os.path.join(includes_dir, category, example), exist_ok=True)
                for script in find_files(os.path.join(example_src_dir, "example"), "*.script|*.gui_script|*.vp|*.fp"):
                    file, ext = os.path.splitext(os.path.basename(script))
                    tgt = os.path.join(includes_dir, category, example, file + "_" + ext.replace(".", "") + ".md")
                    shutil.copyfile(script, tgt)

                print("...copying images")
                for image in find_files(example_src_dir, "*.png|*.jpg|*.gif|*.webp|*.webm"):
                    tgt = os.path.join(example_dst_dir, os.path.basename(image))
                    shutil.copyfile(image, tgt)

        print("...generating index")
        index_file = os.path.join("_data", "examplesindex.json")
        if os.path.exists(index_file):
            os.remove(index_file)
        examplesindex.sort(key=lambda x: x.get("path").lower())
        write_as_json(os.path.join("_data", "examplesindex.json"), examplesindex)

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
            "--platform", "js-web",
            "--architectures", "wasm-web",
            "--variant", "debug",
            "resolve", "distclean", "build", "bundle"
        ], cwd=input_dir)

        codepad_dir = "codepad"
        rmcopytree(os.path.join(input_dir, "build", "default", "DefoldCodePad"), codepad_dir)


def fix_tags_case(list):
    if list:
        for i,v in enumerate(list):
            if v.lower() == "gui":
                list[i] = "GUI"
            elif v.lower() == "ai":
                list[i] = "AI"
            elif v.islower():
                list[i] = v.capitalize()
    return list

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
    rmcopytree(os.path.join(tmp_dir, "asset-portal-master", "assets", "images"), image_dir)

    assetindex = []
    authorindex = {}
    tagindex = {}
    platformindex = {}
    for filename in find_files(os.path.join(tmp_dir, "asset-portal-master", "assets"), "*.json"):
        basename = os.path.basename(filename)
        print("Processing asset: {}".format(basename))
        asset_id = basename.replace(".json", "")

        # copy the data file as-is
        asset_file = os.path.join(asset_data_dir, basename)
        shutil.copyfile(filename, asset_file)

        # read asset and add additional data
        asset = read_as_json(asset_file)
        fix_tags_case(asset["tags"])
        fix_platforms_case(asset["platforms"])
        author_name = asset["author"]
        library_url = asset["library_url"]

        author_id = hashlib.md5(author_name.encode('utf-8')).hexdigest()
        asset["author_id"] = author_id
        asset["asset_url"] = "https://github.com/defold/asset-portal/blob/master/assets/%s.json" % asset_id
        if "github.com" in library_url:
            asset["github_url"] = re.sub(r"(.*github.com/.*?/.*?)/.*", r"\1", library_url)
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

                    # detect language with fallback
                    language = api["info"].get("language")
                    if not language:
                        if namespace.startswith("dm"):
                            print("  No language found in %s, inferring C++ from namespace" % file)
                            api["info"]["language"] = "C++"
                        elif "script_" in api["info"]["path"]:
                            print("  No language found in %s, inferring Lua from path" % file)
                            api["info"]["language"] = "Lua"
                        else:
                            print("  No language found in %s, assuming Lua" % file)
                            api["info"]["language"] = "Lua"
                            # sys.exit(5)

                    # set api type
                    api["info"]["type"] = "Defold " + api["info"]["language"]


                    # make sure file is only the filename and no path
                    if api["info"]["file"] == "":
                        api["info"]["file"] = os.path.basename(api["info"]["path"])
                    elif str.find(api["info"]["file"], "/") != -1:
                        api["info"]["file"] = os.path.basename(api["info"]["file"])

                    # generate include path for C++ files
                    if language == "C++":
                        dmsdk_index = str.find(api["info"]["path"], "dmsdk/")
                        api["info"]["include"] = api["info"]["path"]
                        if dmsdk_index != -1:
                            api["info"]["include"] = api["info"]["path"][dmsdk_index:]

                    # create the key by which we index and collect APIs
                    namespace_key = namespace
                    language = api["info"]["language"]
                    if language == "C++":
                        # namespace_key = namespace_key + "-cpp"
                        namespace_key = api["info"]["path"].replace("..", "").replace("/", "-").replace(".", "-")
                    elif language == "C#":
                        # namespace_key = namespace_key + "-cs"
                        namespace_key = api["info"]["path"].replace("..", "").replace("/", "-").replace(".", "-")
                    else:
                        namespace_key = namespace_key + "-" + language
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
            md = Markdown(extensions=['markdown.extensions.fenced_code','markdown.extensions.def_list', 'markdown.extensions.codehilite','markdown.extensions.tables'])
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
                print("  " + json_out_name + " path: " + p + " lang: " + api["info"].get("language"))
                write_as_json(p, api)

                # generate a dummy markdown page with some front matter for each ref doc
                # example: ref/stable/go-lua.md, ref/stable/dmarray-cpp.md etc
                dummy = os.path.join(REF_PAGE_DIR, json_out_name + ".md")
                with open(dummy, "w") as f:
                    fm_branch = branch
                    fm_ref = json_out_name
                    fm_language = api["info"]["language"]
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
                    fm_language = api["info"]["language"]
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
                    "language": api["info"]["language"],
                    "type": api["info"]["type"],
                })

        # add extensions
        extensions_data_dir = os.path.join("_data", "extensions")
        for filename in os.listdir(extensions_data_dir):
            extension = read_as_json(os.path.join(extensions_data_dir, filename))
            refindex.append({
                "namespace": extension["info"]["namespace"],
                "name": extension["info"]["name"],
                "filename": extension["info"]["name"] + "_" + extension["info"]["namespace"],
                "url": "/" + extension["info"]["api"],
                "branch": branch,
                "language": extension["info"]["language"],
                "type": extension["info"]["type"],
            })

        # generate a list of API types
        types = []
        for ref in refindex:
            if ref["type"] not in types:
                types.append(ref["type"])

        # write overview pages
        for type in types:
            filename = "overview_" + type.replace(" ", "").replace("C++", "cpp").lower() + ".md"
            print("  " + filename, branch)
            with open(os.path.join(REF_PAGE_DIR, filename), "w") as f:
                fm_branch = branch
                fm_ref = "overview"
                fm_language = ""
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






def commit_changes(githubtoken):
    if githubtoken is None:
        print("You must specific a GitHub token")
        sys.exit(1)

    call("git config --global user.name 'services@defold.se'")
    call("git config --global user.email 'services@defold.se'")
    call("git add -A")
    # only commit if the diff isn't empty, ie there is a change
    # https://stackoverflow.com/a/8123841/1266551
    call("git diff-index --quiet HEAD || git commit -m 'Site changes [skip-ci]'")
    call("git push 'https://%s@github.com/defold/defold.github.io.git' HEAD:master" % (githubtoken))


ALL_COMMANDS = [ "all", "help", "docs", "refdoc", "asset-portal", "games-showcase", "examples", "codepad", "commit", "extensions" ]
ALL_COMMANDS.sort()

parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (' + ', '.join(ALL_COMMANDS) + ')')
parser.add_argument("--githubtoken", dest="githubtoken", help="Authentication token for GitHub API and ")
parser.add_argument("--extension", dest="extensions", action='append', help="Which extension to process")
parser.add_argument("--download", dest="download", action='store_true', help="Download updated content for the command(s) in question")
args = parser.parse_args()

help = """
COMMANDS:
docs = Process the docs (manuals, tutorials and faq)
refdoc = Process the API reference
asset-portal = Process the assets list (from asset-portal)
games-showcase = Process the games list (from games-showcase)
examples = Build the examples
codepad = Build the Defold CodePad
commit = Commit changed files (requires --githubtoken)
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
        process_examples(download = args.download)
    elif command == "refdoc":
        process_refdoc(download = args.download)
    elif command == "asset-portal":
        process_asset_portal(download = args.download)
    elif command == "games-showcase":
        process_games_showcase(download = args.download)
    elif command == "codepad":
        process_codepad(download = args.download)
    elif command == "commit":
        commit_changes(args.githubtoken)
    else:
        print("Unknown command {}".format(command))
