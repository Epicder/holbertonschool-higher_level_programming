#!/usr/bin/python3

""" load a json file"""
import json


def load_from_json_file(filename):
    """code"""
    with open(filename, mode="r") as mfile:
        json.load(mfile)
