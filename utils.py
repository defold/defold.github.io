import json
import os
import shutil


def rmtree(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def list_files(dir, ext, sort = False):
    files = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            files.append(file)
    if sort:
        files.sort()
    return files


def read_as_string(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


def read_as_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def write_as_string(filename, s):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)
