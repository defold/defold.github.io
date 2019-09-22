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
from argparse import ArgumentParser
from contextlib import contextmanager

SHA1 = None

DOCS_ZIP = "doc-master.zip"
EXAMPLES_ZIP = "examples-master.zip"
CODEPAD_ZIP = "codepad-master.zip"
AWESOME_ZIP = "awesome-defold-master.zip"
REFDOC_ZIP = "refdoc.zip"

ASSET_MD_FRONTMATTER = """---
layout: asset
asset: {}
---
"""

REFDOC_MD_FRONTMATTER = """---
layout: ref
ref: {}
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


def download_string(url):
    handle = urllib.urlopen(url)
    return handle.read()


def get_sha1():
    global SHA1
    if not SHA1:
        print(download_string("https://d.defold.com/stable/info.json"))
        info = json.loads(download_string("https://d.defold.com/stable/info.json"))
        SHA1 = info["sha1"]
    return SHA1


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
    replace_in_file(file, r"{.left}", r"")


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

        print("Processing doc")
        print("...manuals")
        manuals_dir = "_manuals"
        if os.path.exists(manuals_dir):
            shutil.rmtree(manuals_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "manuals"), manuals_dir)
        for filename in find_files(manuals_dir, "*.md"):
            process_doc_file(filename)

        print("...faq")
        faq_dir = "_faq"
        if os.path.exists(faq_dir):
            shutil.rmtree(faq_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "faq"), faq_dir)

        print("...shared includes")
        shared_includes_dir = os.path.join("_includes", "shared")
        if os.path.exists(shared_includes_dir):
            shutil.rmtree(shared_includes_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "shared"), shared_includes_dir)
        shutil.rmtree(os.path.join(shared_includes_dir, "images"))
        for filename in find_files(shared_includes_dir, "*.md"):
            process_doc_file(filename)

        print("...shared images")
        shared_images_dir = os.path.join("shared", "images")
        if os.path.exists(shared_images_dir):
            shutil.rmtree(shared_images_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "shared", "images"), shared_images_dir)

        print("...tutorials")
        tutorials_dir = "_tutorials"
        if os.path.exists(tutorials_dir):
            shutil.rmtree(tutorials_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "tutorials"), tutorials_dir)
        for filename in find_files(tutorials_dir, "*.md"):
            process_doc_file(filename)

        print("...index")
        index_file = os.path.join("_data", "learnindex.json")
        if os.path.exists(index_file):
            os.remove(index_file)
        shutil.copyfile(os.path.join(tmp_dir, "doc-master", "docs", "en", "en.json"), index_file)

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

        print("..building app")
        shutil.copyfile(bob_jar, os.path.join(tmp_dir, bob_jar))
        input_dir = os.path.join(tmp_dir, "examples-master")
        subprocess.call([ "java", "-jar", os.path.join(tmp_dir, bob_jar), "--archive", "--platform", "js-web", "resolve", "build", "bundle" ], cwd=input_dir)

        print("...copying app")
        examples_dir = "examples"
        if os.path.exists(examples_dir):
            shutil.rmtree(examples_dir)
        shutil.copytree(os.path.join(input_dir, "build", "default", "Defold-examples"), examples_dir)

        print("...processing index.html")
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\!DOCTYPE html\>.*\<body\>", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "\<\/body\>.*", "", flags=re.DOTALL)
        replace_in_file(os.path.join(examples_dir, "index.html"), "resize_game_canvas\(\)\;", "")
        replace_in_file(os.path.join(examples_dir, "index.html"), "window.addEventListener.*", "")
        replace_in_file(os.path.join(examples_dir, "index.html"), 'width=\"720\" height=\"720\"', 'width="680" height="680"')

        replace_in_file(os.path.join(examples_dir, "index.html"), "engine_arguments: \[", "engine_arguments: [ '--config=examples.start={{ page.collection }}'")
        shutil.copyfile(os.path.join(examples_dir, "index.html"), "_includes/example.html")

        print("...copying markdown")
        examplesindex = []
        for filename in find_files(os.path.join(tmp_dir, "examples-master", "examples"), "*.md"):
            basename = os.path.basename(filename)
            collection = filename.replace(tmp_dir, "").replace("/examples-master/examples/", "").replace("/" + basename, "")
            examplesindex.append({
                "collection": collection,
                "category": collection.split("/")[0].upper(),
                "name": collection.split("/")[1].replace("_", " ").capitalize(),
                "path": collection.split("/")[1]
            })
            replace_in_file(filename, "title:", "layout: example\ncollection: {}\ntitle:".format(collection))
            shutil.copyfile(filename, os.path.join("examples", basename))

        print("...copying images")
        for filename in find_files(os.path.join(tmp_dir, "examples-master", "examples"), "*.png"):
            shutil.copyfile(filename, os.path.join("examples", os.path.basename(filename)))
        for filename in find_files(os.path.join(tmp_dir, "examples-master", "examples"), "*.jpg"):
            shutil.copyfile(filename, os.path.join("examples", os.path.basename(filename)))

        print("...copying scripts")
        includes_dir = "_includes/examples"
        if os.path.exists(includes_dir):
            shutil.rmtree(includes_dir)
        os.mkdir(includes_dir)
        for filename in find_files(os.path.join(tmp_dir, "examples-master", "examples"), "*.script"):
            shutil.copyfile(filename, os.path.join(includes_dir, os.path.basename(filename).replace(".script", "_script.md")))
        for filename in find_files(os.path.join(tmp_dir, "examples-master", "examples"), "*.gui_script"):
            shutil.copyfile(filename, os.path.join(includes_dir, os.path.basename(filename).replace(".gui_script", "_gui_script.md")))

        print("...generating index")
        index_file = os.path.join("_data", "examplesindex.json")
        if os.path.exists(index_file):
            os.remove(index_file)
        with open(os.path.join("_data", "examplesindex.json"), "w") as f:
            json.dump(examplesindex, f, indent=2)


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
        if os.path.exists(codepad_dir):
            shutil.rmtree(codepad_dir)
        shutil.copytree(os.path.join(input_dir, "build", "default", "DefoldCodePad"), codepad_dir)



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


        # Jekyll collection
        collection_dir = "assets"
        if os.path.exists(collection_dir):
            shutil.rmtree(collection_dir)
        os.mkdir(collection_dir)

        # Jekyll data
        data_dir = os.path.join("_data", "assets")
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        os.mkdir(data_dir)

        # image data
        image_dir = os.path.join("images", "assets")
        if os.path.exists(image_dir):
            shutil.rmtree(image_dir)
        shutil.copytree(os.path.join(tmp_dir, "awesome-defold-master", "assets", "images", "assets"), image_dir)

        assetindex = []
        for filename in find_files(os.path.join(tmp_dir, "awesome-defold-master", "assets"), "*.json"):
            basename = os.path.basename(filename)

            # copy the data file as-is
            shutil.copyfile(filename, os.path.join(data_dir, basename))

            # generate a dummy markdown page with some front matter for each ref doc
            with open(os.path.join(collection_dir, basename.replace(".json", ".md")), "w") as f:
                f.write(ASSET_MD_FRONTMATTER.format(basename.replace(".json", "")))

            # build refdoc indexs
            with open(filename) as f:
                r = json.load(f)
                assetindex.append({
                    "id": basename.replace(".json", ""),
                    "tags": r["tags"],
                    "platforms": r["platforms"]
                })

        # write asset index
        with open(os.path.join("_data", "assetindex.json"), "w") as f:
            json.dump(assetindex, f, indent=2)



def process_refdoc(download = False):
    if download:
        if os.path.exists(REFDOC_ZIP):
            os.remove(REFDOC_ZIP)
        download_file("http://d.defold.com/archive/{}/engine/share/ref-doc.zip".format(get_sha1()), ".", REFDOC_ZIP)

    if not os.path.exists(REFDOC_ZIP):
        print("File {} does not exist".format(REFDOC_ZIP))
        sys.exit(1)

    with tmpdir() as tmp_dir:
        shutil.copyfile(REFDOC_ZIP, os.path.join(tmp_dir, REFDOC_ZIP))
        unzip(os.path.join(tmp_dir, REFDOC_ZIP), tmp_dir)

        # Jekyll collection
        collection_dir = "ref"
        if os.path.exists(collection_dir):
            shutil.rmtree(collection_dir)
        os.mkdir(collection_dir)

        # Jekyll data
        data_dir = os.path.join("_data", "ref")
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        os.mkdir(data_dir)

        refindex = []
        for file in os.listdir(os.path.join(tmp_dir, "doc")):
            if file.endswith(".json"):
                json_out_name = file.replace("_doc.json", "")
                json_out_file = json_out_name + ".json"

                # copy and rename file
                shutil.copyfile(os.path.join(tmp_dir, "doc", file), os.path.join(data_dir, json_out_file))

                # generate a dummy markdown page with some front matter for each ref doc
                with open(os.path.join(collection_dir, file.replace("_doc.json", ".md")), "w") as f:
                    f.write(REFDOC_MD_FRONTMATTER.format(json_out_name) + REFDOC_MD_BODY)

                # build refdoc indexs
                with open(os.path.join(tmp_dir, "doc", file)) as f:
                    r = json.load(f)
                    refindex.append({
                        "namespace": r["info"]["namespace"],
                        "filename": json_out_name,
                    })

        # write refdoc index
        with open(os.path.join("_data", "refindex.json"), "w") as f:
            json.dump(refindex, f, indent=2)



parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (docs, examples, refdoc, assets, codepad, help)')
parser.add_argument("--download", dest="download", action='store_true', help="Download updated content for the command(s) in question")
args = parser.parse_args()

help = """
COMMANDS:
docs = Process the docs (manuals, tutorials and faq)
refdoc = Process the API reference
assets = Process the asset portal list
examples = Build the examples
codepad = Build the Defold CodePad
"""

for command in args.commands:
    if command == "help":
        parser.print_help()
        print(help)
        sys.exit(0)
    elif command == "docs":
        process_docs(args.download)
    elif command == "examples":
        process_examples(args.download)
    elif command == "refdoc":
        process_refdoc(args.download)
    elif command == "assets":
        process_assets(args.download)
    elif command == "codepad":
        process_codepad(args.download)
    else:
        print("Unknown command {}".format(command))
