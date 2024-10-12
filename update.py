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
from argparse import ArgumentParser
from contextlib import contextmanager
import lunr
from lunr import trimmer

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
type: {}
title: API reference ({})
---
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

def rmtree(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)

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


def find_files(root_dir, file_pattern):
    matches = []
    for root, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            fullname = os.path.join(root, filename)
            if fnmatch.fnmatch(filename, file_pattern):
                matches.append(os.path.join(root, filename))
    return matches

def read_as_string(filename):
    with open(filename) as f:
        return f.read()

def read_as_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_as_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def replace_in_file(filename, old, new, flags=None):
    with open(filename) as f:
        if flags is None:
            content = re.sub(old, new, f.read())
        else:
            content = re.sub(old, new, f.read(), flags=flags)

    with open(filename, "w") as f:
        f.write(content)


def append_to_file(filename, s):
    with open(filename, "a") as f:
        f.write(s)



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


def process_docs(download = False):
    if download:
        if os.path.exists(DOCS_ZIP):
            os.remove(DOCS_ZIP)
        download_file("https://github.com/defold/doc/archive/master.zip", ".", DOCS_ZIP)

    if not os.path.exists(DOCS_ZIP):
        print("File {} does not exists".format(DOCS_ZIP))
        sys.exit(1)

    DOC_DIR=os.environ.get('DM_DOC_DIR', None)

    with tmpdir() as tmp_dir:
        if not DOC_DIR:
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
                    replace_in_file(filename, r"title\:", r"layout: manual\ntitle:")
                    replace_in_file(filename, r"title\:", r"language: {}\ntitle:".format(language))
                    replace_in_file(filename, r"title\:", r"github: {}\ntitle:".format("https://github.com/defold/doc"))
                    if language != "en":
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
                    replace_in_file(filename, r"title\:", r"language: {}\ntitle:".format(language))
                    replace_in_file(filename, r"title\:", r"layout: faq\ntitle:")
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
            replace_in_file(filename, r"title\:", r"layout: tutorial\ntitle:")

        print("...courses")
        courses_src_dir = os.path.join(DOC_DIR, "docs", "en", "courses")
        courses_dst_dir = "courses"
        rmcopytree(courses_src_dir, courses_dst_dir)
        for filename in find_files(courses_dst_dir, "*.md"):
            process_doc_file(filename, "en")
            replace_in_file(filename, r"title\:", r"layout: course\ntitle:")

        # figure out in which languages each manual exists
        print("...index (incl. languages)")
        for section in index["navigation"]["manuals"]:
            for item in section["items"]:
                item["languages"] = []
                if not item["path"].startswith("http"):
                    path = item["path"][1:]
                    for language in languages["languages"].keys():
                        if os.path.exists(get_language_specific_dir(language, path + ".md")):
                            item["languages"].append(language)
        write_as_json(index_file, index)

        print("...shared images")
        shared_images_src_dir = os.path.join(DOC_DIR, "docs", "en", "shared", "images")
        shared_images_dst_dir = os.path.join("shared", "images")
        rmcopytree(shared_images_src_dir, shared_images_dst_dir)

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
            subp = parse_extension_parameters(p.get("parameters")) + parse_extension_parameters(p.get("members"))
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
                print("HAS MEMBERS")
                elements.extend(parse_script_api_members(api_name + "." + member_name, m))
        else:
            element["name"] = m.get("name", "")
        examples = []
        for e in m.get("examples", []):
            desc = e.get("desc", "")
            examples.append(md.convert(desc))
        element["examples"] = "".join(examples)
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
        replace_in_file(index, r"title\:", r"layout: manual\ntitle:")
        replace_in_file(index, r"title\:", r"language: en\ntitle:")
        replace_in_file(index, r"title\:", r"github: {}\ntitle:".format(github_url))
        process_doc_file(index, "en")

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
            append_to_file(index, "[API Reference - {}](/{}/{}_api)\n".format(api_name, extension_dir, api_name))

            # generate a dummy markdown page with some front matter for the api doc
            api_filename = os.path.join(extension_dir, api_name + "_api.html")
            with open(api_filename, "w") as f:
                fm_branch = "stable"
                fm_ref = extension_name + "_" + api_name
                fm_type = "extension"
                fm_title = extension_name
                f.write(REFDOC_MD_FRONTMATTER.format(fm_branch, fm_ref, fm_type, fm_title) + REFDOC_MD_BODY)

            info["group"] = "EXTENSIONS"
            info["description"] = api.get("desc", "")
            info["namespace"] = api_name
            info["name"] = extension_name
            info["brief"] = api_name
            info["api"] = os.path.join(extension_dir, api_name + "_api")

            elements.extend(parse_script_api_members(api_name, api))

            # write the json data file
            extension_data_dir = os.path.join("_data", "extensions")
            makedirs(extension_data_dir)
            extension_data_file = os.path.join(extension_data_dir, extension_name + "_" + api_name + ".json")
            write_as_json(extension_data_file, refdoc)


def process_examples(download = False):
    if download:
        if os.path.exists(EXAMPLES_ZIP):
            os.remove(EXAMPLES_ZIP)
        download_file("https://github.com/defold/examples/archive/master.zip", ".", EXAMPLES_ZIP)
        download_bob(get_sha1())

    if not os.path.exists(EXAMPLES_ZIP):
        print("File {} does not exist".format(EXAMPLES_ZIP))
        sys.exit(1)

    bob_jar = get_bob_filename(get_sha1())
    if not os.path.exists(bob_jar):
        print("File {} does not exist".format(bob_jar))
        sys.exit(1)

    print("Processing examples")
    with tmpdir() as tmp_dir:
        shutil.copyfile(EXAMPLES_ZIP, os.path.join(tmp_dir, EXAMPLES_ZIP))
        unzip(os.path.join(tmp_dir, EXAMPLES_ZIP), tmp_dir)
        unzipped_examples_dir = os.path.join(tmp_dir, "examples-master", "examples")

        print("..building app")
        shutil.copyfile(bob_jar, os.path.join(tmp_dir, bob_jar))
        input_dir = os.path.join(tmp_dir, "examples-master")
        subprocess.call([ "java", "-jar", os.path.join(tmp_dir, bob_jar), "--archive", "--platform", "js-web", "--variant", "debug", "resolve", "build", "bundle" ], cwd=input_dir)

        print("...copying app")
        examples_dir = "examples"
        rmcopytree(os.path.join(input_dir, "build", "default", "Defold-examples", "archive"), os.path.join(examples_dir, "archive"))
        for file in ["Defoldexamples_asmjs.js", "Defoldexamples_wasm.js", "Defoldexamples.wasm", "dmloader.js", "index.html"]:
            shutil.copyfile(os.path.join(input_dir, "build", "default", "Defold-examples", file), os.path.join(examples_dir, file))

        print("...processing index.html")
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\!DOCTYPE html\>.*\<body\>", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\/body\>.*", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "\(\)\;", "")
        replace_in_file(os.path.join(examples_dir, "index.html"), 'width=\"720\" height=\"720\"', 'width="680" height="680" style="max-width:100%"')
        replace_in_file(os.path.join(examples_dir, "index.html"), 'dmloader.js', '/examples/dmloader.js')
        replace_in_file(os.path.join(examples_dir, "index.html"), 'EngineLoader\.load\(\"canvas\", \"Defoldexamples\"\);', EXAMPLES_ENGINE_LOADER)
        os.rename(os.path.join(examples_dir, "index.html"), "_includes/example.html")

        print("...copying markdown")
        examplesindex = []
        for filename in find_files(unzipped_examples_dir, "*.md"):
            basename = os.path.basename(filename)
            collection = filename.replace(tmp_dir, "").replace("/examples-master/examples/", "").replace("/" + basename, "")
            name = collection.split("/")[1].replace("_", " ").capitalize()
            permalink = "examples/" + collection + "/"

            try:
                for data in yaml.safe_load_all(read_as_string(filename)):
                    if "name" in data:
                        name = data.get("name")
                    break
            except yaml.YAMLError:
                pass

            examplesindex.append({
                "collection": collection,
                "category": collection.split("/")[0].upper(),
                "name": name,
                "path": collection
            })
            replace_in_file(filename, "title:", "layout: example\npermalink: {}\ncollection: {}\ntitle:".format(permalink, collection))

            md_file = os.path.join(examples_dir, filename.replace(unzipped_examples_dir, "")[1:])
            makedirs(os.path.dirname(md_file))
            shutil.copyfile(filename, md_file)

        print("...copying images")
        for filename in find_files(unzipped_examples_dir, "*.png"):
            png_file = os.path.join(examples_dir, filename.replace(unzipped_examples_dir, "")[1:])
            makedirs(os.path.dirname(png_file))
            shutil.copyfile(filename, png_file)
        for filename in find_files(unzipped_examples_dir, "*.jpg"):
            jpg_file = os.path.join(examples_dir, filename.replace(unzipped_examples_dir, "")[1:])
            makedirs(os.path.dirname(jpg_file))
            shutil.copyfile(filename, jpg_file)

        print("...copying scripts")
        includes_dir = "_includes/examples"
        rmmkdir(includes_dir)
        for ext in ["script", "gui_script", "vp", "fp"]:
            for source in find_files(unzipped_examples_dir, "*." + ext):
                target = os.path.join(includes_dir, source.replace(unzipped_examples_dir, "")[1:]).replace("." + ext, "_" + ext + ".md")
                makedirs(os.path.dirname(target))
                shutil.copyfile(source, target)

        print("...generating index")
        index_file = os.path.join("_data", "examplesindex.json")
        if os.path.exists(index_file):
            os.remove(index_file)
        write_as_json(os.path.join("_data", "examplesindex.json"), examplesindex)


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
        subprocess.call([ "java", "-jar", os.path.join(tmp_dir, bob_jar), "--archive", "--platform", "js-web", "resolve", "distclean", "build", "bundle" ], cwd=input_dir)

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
        write_as_json(asset_file, asset)

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
    write_as_json(ASSETINDEX_JSON, assetindex)

    # write author index
    authorlist = authorindex.values()
    authorlist = sorted(authorlist, key=lambda x: x.get("name").lower())
    write_as_json(AUTHORINDEX_JSON, authorlist)

    # write author data and a dummy markdown page with front matter
    for author in authorlist:
        author["assets"].sort(key=lambda x: x.get("id"))
        filename = os.path.join(author_data_dir, author["id"] + ".json")
        write_as_json(filename, author)
        with open(os.path.join(author_collection_dir, author["id"] + ".md"), "w") as f:
            f.write(AUTHOR_MD_FRONTMATTER.format(author["id"], author["name"]))

    # write tag index
    taglist = tagindex.values()
    taglist = sorted(taglist, key=lambda x: x.get("id").lower())
    write_as_json(TAGINDEX_JSON, taglist)

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
            f.write(json.dumps(tag, indent=2, sort_keys=True))

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

    # read new games
    for filename in find_files(os.path.join(tmp_dir, "games-showcase-master", "games"), "*.json"):
        basename = os.path.basename(filename)
        print("Processing game: {}".format(basename))

        # read new game and add additional data
        game_id = basename.replace(".json", "")
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


LUA_APIS = [ "base", "bit", "coroutine", "debug", "io", "math", "os", "package", "socket", "string", "table" ]

def process_refdoc(download = False):
    refindex = []
    branchindex = [ "alpha", "beta", "stable" ]
    ref_root_dir = "ref"
    rmmkdir(ref_root_dir)

    for branch in branchindex:
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

            for file in os.listdir(os.path.join(tmp_dir, "doc")):
                if file.endswith(".json"):
                    api = read_as_json(os.path.join(tmp_dir, "doc", file))
                    # ignore empty APIs (such as those moved to extensions)
                    if len(api["elements"]) > 0:
                        json_out_name = file.replace("_doc.json", "")
                        json_out_file = json_out_name + ".json"

                        api["elements"].sort(key=lambda x: x.get("name").lower())
                        write_as_json(os.path.join(REF_DATA_DIR, json_out_file), api)

                        namespace = api["info"]["namespace"]
                        api_type = "defold"
                        if namespace in LUA_APIS:
                            api_type = "lua"
                        elif namespace.startswith("dm") or namespace == "sharedlibrary":
                            api_type = "c"

                        print("REFDOC " + json_out_name + " type: " + api_type)

                        # generate a dummy markdown page with some front matter for each ref doc
                        with open(os.path.join(REF_PAGE_DIR, file.replace("_doc.json", ".md")), "w") as f:
                            f.write(REFDOC_MD_FRONTMATTER.format(branch, json_out_name, api_type, json_out_name) + REFDOC_MD_BODY)

                        # build refdoc index
                        refindex.append({
                            "namespace": namespace,
                            "name": api["info"]["name"],
                            "filename": json_out_name,
                            "url": "/ref/" + branch + "/" + json_out_name,
                            "branch": branch,
                            "type": api_type
                        })

        # add extensions
        extensions_data_dir = os.path.join("_data", "extensions")
        for filename in os.listdir(extensions_data_dir):
            extension = read_as_json(os.path.join(extensions_data_dir, filename))
            refindex.append({
                "namespace": extension["info"]["namespace"],
                "name": extension["info"]["name"],
                "url": "/" + extension["info"]["api"],
                "branch": branch,
                "type": "extension"
            })

    # copy stable files to ref/ for backwards compatibility
    for item in os.listdir(os.path.join("ref", "stable")):
        s = os.path.join("ref", "stable", item)
        d = os.path.join("ref", item)
        if not os.path.isdir(s):
            shutil.copy2(s, d)


    # write refdoc index
    write_as_json(os.path.join("_data", "refindex.json"), refindex)

    # write branch index
    write_as_json(os.path.join("_data", "branchindex.json"), branchindex)


def process_file_for_indexing(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', ' ')

        # replace the math notations
        data = re.sub("\$\$.*?\$\$", " ", data)

        # remove the html tags (but leave the text behind)
        data = re.sub(r"<(.*?)>(.*?)</\1>", "\2", data)

        # remove closed html tags "<tag />"
        data = re.sub(r"<\w+?\s.*?/>", " ", data)

        # Cleanup markdown links
        data = re.sub("\[(.*?)\]\(.*?\)", "\1", data)

        # finally, remove certain characters
        # (do this last, so that any regexp above won't break)
        #data = re.sub(r"(=|\.|\(|\))+", " ", data)
        data = re.sub(r"(=|\(|\))+", " ", data)

        return data


def generate_searchindex():
    searchindex = []

    def append_ref_doc(filename, data):
        searchindex.append({
            "id": filename.replace("_data/", "").replace(".json", ""),
            "type": "refdoc",
            "data": data
        })

    def append_manual(filename, data):
        searchindex.append({
            "id": filename.replace("_", "").replace(".md", ""),
            "type": "manual",
            "data": data
        })

    def append_asset(filename, data):
        searchindex.append({
            "id": filename.replace("_data/", "").replace(".json", ""),
            "type": "asset",
            "data": data
        })

    for filename in find_files("manuals", "*.md"):
        data = process_file_for_indexing(filename)
        append_manual(filename, data)

    for filename in find_files(os.path.join("_data", "assets"), "*.json"):
        r = read_as_json(filename)
        id = os.path.basename(filename).replace(".json", "")
        append_asset(filename, id + " " + r["name"] + " " + r["description"])

    for filename in find_files(os.path.join("_data", "ref", "stable"), "*.json"):
        r = read_as_json(filename)
        for element in r["elements"]:
            name = element["name"]
            append_ref_doc(filename, name)

            if "." in name:
                for part in name.split("."):
                    append_ref_doc(filename, part)
            elif "::" in name:
                for part in name.split("::"):
                    append_ref_doc(filename, part)

    # manually create a builder without stemming, stop words etc
    # if we use the standard builder pipeline functions we will end up
    # with partial search words like go.get_posit instead of go.get_position
    builder = lunr.builder.Builder()
    builder.pipeline.add(trimmer.trimmer)
    builder.ref("id")
    for field in ('type', 'data'):
        if isinstance(field, dict):
            builder.field(**field)
        else:
            builder.field(field)
    for document in searchindex:
        if isinstance(document, (tuple, list)):
            builder.add(document[0], attributes=document[1])
        else:
            builder.add(document)
    lunrindex = builder.build()
    # lunrindex = lunr.lunr(ref='id', fields=('type', 'data'), documents=searchindex)

    write_as_json("searchindex.json", lunrindex.serialize())


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


ALL_COMMANDS = [ "docs", "refdoc", "asset-portal", "games-showcase", "examples", "codepad", "commit", "searchindex", "extensions" ]
ALL_COMMANDS.sort()

parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (' + ', '.join(ALL_COMMANDS) + ', all, help)')
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
searchindex = Update the static Lunr search index
extensions = Process the docs for official extensions (use --extension to specify which extensions to process)
all = Run all of the above commands
help = Show this help
"""

if "all" in args.commands:
    args.commands.remove("all")
    commands = []
    commands.extend(ALL_COMMANDS)
    commands.extend(args.commands)
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
    elif command == "searchindex":
        generate_searchindex()
    elif command == "commit":
        commit_changes(args.githubtoken)
    else:
        print("Unknown command {}".format(command))
