#!/usr/bin/python3

""" save a json file"""
import json

def save_to_json_file(my_obj, filename):
    """code"""
    with open(filename, mode="w") as mfile:
        json.dump(my_obj, mfile)
