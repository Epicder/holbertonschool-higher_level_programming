#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as jfile:
        json.dump(data, jfile)


def load_and_deserialize(filename):
    with open(filename, 'r') as jfile:
        code = json.load(jfile)
    return code
