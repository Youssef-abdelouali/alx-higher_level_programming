#!/usr/bin/python3
"""Defines a function to check object class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to examine.
        a_class (type): The class to compare against the type of obj. 
    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
