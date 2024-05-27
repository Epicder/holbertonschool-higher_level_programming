#!/usr/bin/python3
""" provides a function to list the attributes and methods of an obj"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
