#!/usr/bin/env python

import urllib
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
import urlparse
import hashlib
from argparse import ArgumentParser
from contextlib import contextmanager
import lunr

SHA1 = {}

DOCS_ZIP = "doc-master.zip"
EXAMPLES_ZIP = "examples-master.zip"
CODEPAD_ZIP = "codepad-master.zip"
AWESOME_ZIP = "awesome-defold-master.zip"

ASSETINDEX_JSON = os.path.join("_data", "assetindex.json")
AUTHORINDEX_JSON = os.path.join("_data", "authorindex.json")
TAGINDEX_JSON = os.path.join("_data", "tagindex.json")
PLATFORMINDEX_JSON = os.path.join("_data", "platformindex.json")

REF_DATA_DIR = os.path.join("_data", "ref")

ASSET_MD_FRONTMATTER = """---
layout: asset
asset: {}
title: {}
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
layout: ref
branch: {}
ref: {}
title: API reference ({})
---
"""
REFDOC_MD_BODY = "{% include anchor_headings.html html=content %}"


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
    urllib.urlretrieve(url, path)
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


def read_as_json(filename):
    with open(filename) as f:
        return json.load(f)


def write_as_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def replace_in_file(filename, old, new, flags=None):
    with open(filename) as f:
        if flags is None:
            content = re.sub(old, new, f.read())
        else:
            content = re.sub(old, new, f.read(), flags=flags)

    with open(filename, "w") as f:
        f.write(content)



def process_doc_file(file):
    replace_in_file(file, r"({{{?)(.*?)(}}}?)", r"{% raw %}\1\2\3{% endraw %}")
    replace_in_file(file, r"{srcset=.*?}", r"")
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


def get_language_specific_dir(language, dir):
    if language != "en":
        dir = os.path.join(language, dir)
    return dir


def process_docs(download = False):
    if download:
        if os.path.exists(DOCS_ZIP):
            os.remove(DOCS_ZIP)
        download_file("https://github.com/defold/doc/archive/master.zip", ".", DOCS_ZIP)

    if not os.path.exists(DOCS_ZIP):
        print("File {} does not exists".format(DOCS_ZIP))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(DOCS_ZIP, os.path.join(tmp_dir, DOCS_ZIP))
        unzip(os.path.join(tmp_dir, DOCS_ZIP), tmp_dir)

        print("Processing docs")

        print("...languages")
        languages = read_as_json(os.path.join(tmp_dir, "doc-master", "docs", "languages.json"))
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
        shutil.copyfile(os.path.join(tmp_dir, "doc-master", "docs", "en", "en.json"), index_file)
        index = read_as_json(index_file)

        for language in languages["languages"].keys():
            print("...manuals ({})".format(language))
            manuals_src_dir = os.path.join(tmp_dir, "doc-master", "docs", language, "manuals")
            if os.path.exists(manuals_src_dir):
                manuals_dst_dir = get_language_specific_dir(language, "manuals")
                rmcopytree(manuals_src_dir, manuals_dst_dir)
                for filename in find_files(manuals_dst_dir, "*.md"):
                    process_doc_file(filename)
                    replace_in_file(filename, r"title\:", r"layout: manual\ntitle:")
                    replace_in_file(filename, r"title\:", r"language: {}\ntitle:".format(language))
                    if language != "en":
                        replace_in_file(filename, r"\/manuals\/", r"/{}/manuals/".format(language))

        print("...faq")
        faq_src_dir = os.path.join(tmp_dir, "doc-master", "docs", "en", "faq")
        faq_dst_dir = "faq"
        rmcopytree(faq_src_dir, faq_dst_dir)
        for filename in find_files(faq_dst_dir, "*.md"):
            process_doc_file(filename)
            replace_in_file(filename, r"title\:", r"layout: text\ntitle:")

        print("...shared includes")
        shared_includes_src_dir = os.path.join(tmp_dir, "doc-master", "docs", "en", "shared")
        shared_includes_dst_dir = os.path.join("_includes", "shared")
        rmcopytree(shared_includes_src_dir, shared_includes_dst_dir)
        shutil.rmtree(os.path.join(shared_includes_dst_dir, "images"))
        for filename in find_files(shared_includes_dst_dir, "*.md"):
            process_doc_file(filename)

        print("...tutorials")
        tutorials_src_dir = os.path.join(tmp_dir, "doc-master", "docs", "en", "tutorials")
        tutorials_dst_dir = "tutorials"
        rmcopytree(tutorials_src_dir, tutorials_dst_dir)
        for filename in find_files(tutorials_dst_dir, "*.md"):
            process_doc_file(filename)
            replace_in_file(filename, r"title\:", r"layout: tutorial\ntitle:")

        # figure in which languages each learn page exists
        print("...index (incl. languages)")
        for categories in index["navigation"]:
            for section in index["navigation"][categories]:
                for item in section["items"]:
                    item["languages"] = []
                    if not item["path"].startswith("http"):
                        path = item["path"][1:]
                        for language in languages["languages"].keys():
                            if os.path.exists(get_language_specific_dir(language, path + ".md")):
                                item["languages"].append(language)
        write_as_json(index_file, index)

        print("...shared images")
        shared_images_src_dir = os.path.join(tmp_dir, "doc-master", "docs", "en", "shared", "images")
        shared_images_dst_dir = os.path.join("shared", "images")
        rmcopytree(shared_images_src_dir, shared_images_dst_dir)

        print("Done")


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
        subprocess.call([ "java", "-jar", os.path.join(tmp_dir, bob_jar), "--archive", "--platform", "js-web", "resolve", "build", "bundle" ], cwd=input_dir)

        print("...copying app")
        examples_dir = "examples"
        rmcopytree(os.path.join(input_dir, "build", "default", "Defold-examples"), examples_dir)

        print("...processing index.html")
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\!DOCTYPE html\>.*\<body\>", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\/body\>.*", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "resize_game_canvas\(\)\;", "")
        replace_in_file(os.path.join(examples_dir, "index.html"), "window.addEventListener.*", "")
        replace_in_file(os.path.join(examples_dir, "index.html"), 'width=\"720\" height=\"720\"', 'width="680" height="680" style="max-width:100%"')
        replace_in_file(os.path.join(examples_dir, "index.html"), 'dmloader.js', '/examples/dmloader.js')
        replace_in_file(os.path.join(examples_dir, "index.html"), '\"archive\"', '"/examples/archive"')
        replace_in_file(os.path.join(examples_dir, "index.html"), 'engineJS\.src = \'Defoldexamples', 'engineJS.src = \'/examples/Defoldexamples')
        replace_in_file(os.path.join(examples_dir, "index.html"), "engine_arguments: \[", "engine_arguments: [ '--config=examples.start={{ page.collection }}'")
        shutil.copyfile(os.path.join(examples_dir, "index.html"), "_includes/example.html")

        print("...copying markdown")
        examplesindex = []
        for filename in find_files(unzipped_examples_dir, "*.md"):
            basename = os.path.basename(filename)
            collection = filename.replace(tmp_dir, "").replace("/examples-master/examples/", "").replace("/" + basename, "")
            permalink = "examples/" + collection + "/"
            examplesindex.append({
                "collection": collection,
                "category": collection.split("/")[0].upper(),
                "name": collection.split("/")[1].replace("_", " ").capitalize(),
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
        for filename in find_files(unzipped_examples_dir, "*.script"):
            script_file = os.path.join(includes_dir, filename.replace(unzipped_examples_dir, "")[1:]).replace(".script", "_script.md")
            makedirs(os.path.dirname(script_file))
            shutil.copyfile(filename, script_file)
        for filename in find_files(unzipped_examples_dir, "*.gui_script"):
            script_file = os.path.join(includes_dir, filename.replace(unzipped_examples_dir, "")[1:]).replace(".gui_script", "_gui_script.md")
            makedirs(os.path.dirname(script_file))
            shutil.copyfile(filename, script_file)

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
            if v.islower():
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

def process_assets(download = False):
    if download:
        if os.path.exists(AWESOME_ZIP):
            os.remove(AWESOME_ZIP)
        download_file("https://github.com/defold/awesome-defold/archive/master.zip", ".", AWESOME_ZIP)

    if not os.path.exists(AWESOME_ZIP):
        print("File {} does not exist".format(AWESOME_ZIP))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(AWESOME_ZIP, os.path.join(tmp_dir, AWESOME_ZIP))
        unzip(os.path.join(tmp_dir, AWESOME_ZIP), tmp_dir)

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
        rmcopytree(os.path.join(tmp_dir, "awesome-defold-master", "assets", "images", "assets"), image_dir)

        assetindex = []
        authorindex = {}
        tagindex = {}
        platformindex = {}
        for filename in find_files(os.path.join(tmp_dir, "awesome-defold-master", "assets"), "*.json"):
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
            author_name = asset["author"].encode('utf-8')
            author_id = hashlib.md5(author_name).hexdigest()
            asset["author_id"] = author_id
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

            # generate a dummy markdown page with some front matter for each asset
            with open(os.path.join(asset_collection_dir, basename.replace(".json", ".md")), "w") as f:
                f.write(ASSET_MD_FRONTMATTER.format(asset_id, asset["name"]))

        # write asset index
        write_as_json(ASSETINDEX_JSON, assetindex)

        # write author index
        authorlist = authorindex.values()
        authorlist.sort(key=lambda x: x.get("name").lower())
        write_as_json(AUTHORINDEX_JSON, authorlist)

        # write author data and a dummy markdown page with front matter
        for author in authorlist:
            author["assets"].sort(key=lambda x: x.get("id"))
            filename = os.path.join(author_data_dir, author["id"] + ".json")
            with open(filename, "w") as f:
                f.write(json.dumps(author, indent=2, sort_keys=True))
            with open(os.path.join(author_collection_dir, author["id"] + ".md"), "w") as f:
                f.write(AUTHOR_MD_FRONTMATTER.format(author["id"], author["name"]))

        # write tag index
        taglist = tagindex.values()
        taglist.sort(key=lambda x: x.get("id").lower())
        write_as_json(TAGINDEX_JSON, taglist)

        # write platform index
        platformlist = platformindex.values()
        platformlist.sort(key=lambda x: x.get("id").lower())
        write_as_json(PLATFORMINDEX_JSON, platformlist)

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
                    json_out_name = file.replace("_doc.json", "")
                    json_out_file = json_out_name + ".json"

                    # copy and rename file
                    shutil.copyfile(os.path.join(tmp_dir, "doc", file), os.path.join(REF_DATA_DIR, json_out_file))

                    # generate a dummy markdown page with some front matter for each ref doc
                    with open(os.path.join(REF_PAGE_DIR, file.replace("_doc.json", ".md")), "w") as f:
                        f.write(REFDOC_MD_FRONTMATTER.format(branch, json_out_name, json_out_name) + REFDOC_MD_BODY)

                    # build refdoc index
                    r = read_as_json(os.path.join(tmp_dir, "doc", file))
                    refindex.append({
                        "namespace": r["info"]["namespace"],
                        "filename": json_out_name,
                        "branch": branch,
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
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        # data = re.sub("\!\[.*\]\(.*\)", "", data)
        data = re.sub("\[(.*?)\]\(.*?\)", "\1", data)
        return data.decode('utf-8')


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


ALL_COMMANDS = [ "docs", "examples", "refdoc", "assets", "codepad", "searchindex" ]

parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (' + ', '.join(ALL_COMMANDS) + ', all, help)')
parser.add_argument("--githubtoken", dest="githubtoken", help="Authentication token for GitHub API and ")
parser.add_argument("--download", dest="download", action='store_true', help="Download updated content for the command(s) in question")
args = parser.parse_args()

help = """
COMMANDS:
docs = Process the docs (manuals, tutorials and faq)
refdoc = Process the API reference
assets = Process the asset portal list
examples = Build the examples
codepad = Build the Defold CodePad
commit = Commit changed files (requires --githubtoken)
searchindex = Update the static Lunr search index
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
    elif command == "examples":
        process_examples(download = args.download)
    elif command == "refdoc":
        process_refdoc(download = args.download)
    elif command == "assets":
        process_assets(download = args.download)
    elif command == "codepad":
        process_codepad(download = args.download)
    elif command == "searchindex":
        generate_searchindex()
    elif command == "commit":
        commit_changes(args.githubtoken)
    else:
        print("Unknown command {}".format(command))
