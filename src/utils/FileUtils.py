from collections import namedtuple
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def is_file(path):
    return os.path.isfile(path)


def dict_to_struct(dict: dict):
    struct = namedtuple("Struct", dict.keys())(*dict.values())
    return struct
