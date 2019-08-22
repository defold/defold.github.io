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
from subprocess import call
from argparse import ArgumentParser
from contextlib import contextmanager


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


def download_file(url, destination):
    filename = os.path.join(destination, url.rsplit('/', 1)[-1])
    if os.path.exists(filename):
        print("File %s already exists" % (filename))
        sys.exit(1)
    print("Downloading {}".format(url))
    urllib.urlretrieve(url, filename)
    return filename


def download_string(url):
    """ Download data from a URL into a string.
    """
    handle = urllib.urlopen(url)
    return handle.read()


def download_from_builtins(filename, destination):
    stable = download_string("http://d.defold.com/stable/info.json")
    stable_json = json.loads(stable)
    builtins_url = "http://d.defold.com/archive/%s/engine/share/builtins.zip" % (stable_json.get("sha1"))
    with tmpdir() as tmp_dir:
        builtins_file = download_file(builtins_url, tmp_dir)
        unzip(builtins_file, tmp_dir)
        shutil.move(os.path.join(tmp_dir, filename), destination)


def download_android_manifest(destination):
    return download_from_builtins("builtins/manifests/android/AndroidManifest.xml", destination)


def find_files(root_dir, file_pattern):
    matches = []
    for root, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, file_pattern):
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

def process_learn():
    with tmpdir() as tmp_dir:
        shutil.copyfile("master.zip", os.path.join(tmp_dir, "master.zip"))
        # download_file("https://github.com/defold/doc/archive/master.zip", tmp_dir)
        unzip(os.path.join(tmp_dir, "master.zip"), tmp_dir)

        manuals_dir = "manuals"
        if os.path.exists(manuals_dir):
            shutil.rmtree(manuals_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "manuals"), manuals_dir)
        for file in find_files(manuals_dir, "*.md"):
            replace_in_file(file, r"({{{?)(.*?)(}}}?)", r"{% raw %}\1\2\3{% endraw %}")
            replace_in_file(file, r"{srcset=.*?}", r"")
            replace_in_file(file, r"::: sidenote(.*?):::", r"<div class='sidenote' markdown='1'>\1</div>", flags=re.DOTALL)
            replace_in_file(file, r"::: important(.*?):::", r"<div class='important' markdown='1'>\1</div>", flags=re.DOTALL)
            replace_in_file(file, r"\((.*?)#_(.*?)\)", r"(\1#\2)")

        faq_dir = "faq"
        if os.path.exists(faq_dir):
            shutil.rmtree(faq_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "faq"), faq_dir)
        # for file in find_files(faq_dir, "*.md"):
        #     replace_in_file(file, r"\-\-\-(.*?)\-\-\-", r"---\nlayout: text\1---", flags=re.DOTALL)

        tutorials_dir = "tutorials"
        if os.path.exists(tutorials_dir):
            shutil.rmtree(tutorials_dir)
        shutil.copytree(os.path.join(tmp_dir, "doc-master", "docs", "en", "tutorials"), tutorials_dir)
        # for file in find_files(faq_dir, "*.md"):
        #     replace_in_file(file, r"\-\-\-(.*?)\-\-\-", r"---\nlayout: text\1---", flags=re.DOTALL)


def add_argument(parser, short, long, dest, help, default=None, required=False, action="store"):
    parser.add_argument(short, dest=dest, help=help, default=default, required=required, action=action)
    parser.add_argument(long, dest=dest, help=help, default=default, required=required, action=action)


parser = ArgumentParser()
parser.add_argument('commands', nargs="+", help='Commands (learn, help)')
# add_argument(parser, "-o", "--out", "out", "Path to generate files in", default="out")
args = parser.parse_args()

help = """
COMMANDS:
learn = Download the docs and process these.
"""

for command in args.commands:
    if command == "help":
        parser.print_help()
        print(help)
        sys.exit(0)

    if command == "learn":
        process_learn()

# Success!
print("Done")
