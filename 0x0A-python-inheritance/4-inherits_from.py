#!/usr/bin/python3
"""Defines a function for checking inherited class instances."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to   
    Returns:
        True if obj is an inherited instance of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
