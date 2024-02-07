#!/usr/bin/python3
"""Defines a function to lookup object attributes."""


def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings containing the names of the attributes
        of the given object.
    """
    return dir(obj)
