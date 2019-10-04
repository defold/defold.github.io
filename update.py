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
from argparse import ArgumentParser
from contextlib import contextmanager
import lunr

SHA1 = None

DOCS_ZIP = "doc-master.zip"
EXAMPLES_ZIP = "examples-master.zip"
CODEPAD_ZIP = "codepad-master.zip"
AWESOME_ZIP = "awesome-defold-master.zip"
REFDOC_ZIP = "refdoc.zip"

ASSETINDEX_JSON = os.path.join("_data", "assetindex.json")

MANUALS_DIR = "_manuals"
REF_DATA_DIR = os.path.join("_data", "ref")

ASSET_MD_FRONTMATTER = """---
layout: asset
asset: {}
title: {}
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


def get_sha1():
    global SHA1
    if not SHA1:
        info = download_json("https://d.defold.com/stable/info.json")
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
    replace_in_file(file, r"{.left}", r"")
    replace_in_file(file, r"{.icon}", r"")
    replace_in_file(file, r"{.inline}", r"")
    # replace_in_file(file, r"\!\[(.*?)\]\((.*?)\)\{\.inline\}", r"<span style='display: inline'>![\1](\2)</span>")
    replace_in_file(file, r"\(images\/", r"(../images/")
    replace_in_file(file, r"\(\.\.\/shared\/", r"(/shared/")


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
        if os.path.exists(MANUALS_DIR):
            shutil.rmtree(MANUALS_DIR)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "manuals"), MANUALS_DIR)
        for filename in find_files(MANUALS_DIR, "*.md"):
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
        replace_in_file(os.path.join(examples_dir, "index.html"), 'dmloader.js', '/examples/dmloader.js')
        replace_in_file(os.path.join(examples_dir, "index.html"), '\"archive\"', '"/examples/archive"')
        replace_in_file(os.path.join(examples_dir, "index.html"), 'engineJS\.src = \'Defoldexamples', 'engineJS.src = \'/examples/Defoldexamples')
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
        if os.path.exists(codepad_dir):
            shutil.rmtree(codepad_dir)
        shutil.copytree(os.path.join(input_dir, "build", "default", "DefoldCodePad"), codepad_dir)


def update_github_star_count_for_assets(githubtoken):
    if githubtoken is None:
        print("No GitHub token specified")
        sys.exit(1)

    assetindex = read_as_json(ASSETINDEX_JSON)

    for filename in find_files(os.path.join("_data", "assets"), "*.json"):
        asset = read_as_json(filename)
        project_url = asset["project_url"]
        if "github.com" in project_url:
            print("Getting star count for %s" % (asset["name"]))
            repo = re.sub(r"http.?:\/\/github.com\/", "", project_url)

            url = "https://api.github.com/repos/%s/stargazers" % (repo)
            stargazers = github_request(url, githubtoken)
            if stargazers is None:
                return

            stars = len(stargazers)
            print("...%d" % (stars))
            asset["stars"] = stars
            write_as_json(filename, asset)

            id = os.path.basename(filename).replace(".json", "")
            for asset in assetindex:
                if asset["id"] == id:
                    asset["stars"] = stars
                    break

    write_as_json(ASSETINDEX_JSON, assetindex)


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
            asset_id = basename.replace(".json", "")

            # copy the data file as-is
            shutil.copyfile(filename, os.path.join(data_dir, basename))

            # build refdoc indexs
            r = read_as_json(filename)
            assetindex.append({
                "id": asset_id,
                "tags": r["tags"],
                "platforms": r["platforms"]
            })

            # generate a dummy markdown page with some front matter for each ref doc
            with open(os.path.join(collection_dir, basename.replace(".json", ".md")), "w") as f:
                f.write(ASSET_MD_FRONTMATTER.format(asset_id, r["name"]))

        # write asset index
        write_as_json(ASSETINDEX_JSON, assetindex)


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
        if os.path.exists(REF_DATA_DIR):
            shutil.rmtree(REF_DATA_DIR)
        os.mkdir(REF_DATA_DIR)

        refindex = []
        for file in os.listdir(os.path.join(tmp_dir, "doc")):
            if file.endswith(".json"):
                json_out_name = file.replace("_doc.json", "")
                json_out_file = json_out_name + ".json"

                # copy and rename file
                shutil.copyfile(os.path.join(tmp_dir, "doc", file), os.path.join(REF_DATA_DIR, json_out_file))

                # generate a dummy markdown page with some front matter for each ref doc
                with open(os.path.join(collection_dir, file.replace("_doc.json", ".md")), "w") as f:
                    f.write(REFDOC_MD_FRONTMATTER.format(json_out_name) + REFDOC_MD_BODY)

                # build refdoc indexs
                r = read_as_json(os.path.join(tmp_dir, "doc", file))
                refindex.append({
                    "namespace": r["info"]["namespace"],
                    "filename": json_out_name,
                })

        # write refdoc index
        write_as_json(os.path.join("_data", "refindex.json"), refindex)


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

    for filename in find_files(MANUALS_DIR, "*.md"):
        data = process_file_for_indexing(filename)
        append_manual(filename, data)

    for filename in find_files(REF_DATA_DIR, "*.json"):
        r = read_as_json(filename)
        for element in r["elements"]:
            name = element["name"]
            append_ref_doc(filename, name)

            if "." in name:
                for part in name.split("."):
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
    call("git commit -m 'Updated stars [skip-ci]' --allow-empty")
    call("git push 'https://%s@github.com/defold/defold.github.io.git' HEAD:master" % (githubtoken))


ALL_COMMANDS = [ "docs", "examples", "refdoc", "assets", "starcount", "codepad", "searchindex" ]

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
starcount = Add GitHub star count to all assets that have a GitHub project
examples = Build the examples
codepad = Build the Defold CodePad
commit = Commit changed files (requires --githubtoken)
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
    elif command == "starcount":
        update_github_star_count_for_assets(args.githubtoken)
    elif command == "codepad":
        process_codepad(download = args.download)
    elif command == "searchindex":
        generate_searchindex()
    elif command == "commit":
        commit(args.githubtoken)
    else:
        print("Unknown command {}".format(command))
