#!/usr/bin/python3

""" function that read a file"""


def read_file(filename=""):
    """code"""
    with open(filename, mode="r", encoding="utf-8") as mfile:
        text = mfile.read()
        print(text)
