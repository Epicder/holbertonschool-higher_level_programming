#!/usr/bin/python3
""" This module provides a function to list the attributes and methods of an object."""
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
