#!/usr/bin/python3

""" load a json file"""
import json


def load_from_json_file(my_obj, filename):
    """code"""
    with open(filename, mode="r") as mfile:
        json.load(my_obj, mfile)
