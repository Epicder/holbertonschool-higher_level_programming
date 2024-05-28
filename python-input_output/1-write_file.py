#!/usr/bin/python3

"""retrun the n of characters in a string"""


def write_file(filename="", text=""):
    """code"""
    with open(filename, mode="w", encoding="utf-8") as mfile:
        mfile.write(text)
        txt = len(text)
        return txt
