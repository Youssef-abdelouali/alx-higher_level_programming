#!/usr/bin/python3
"""Defines a function for checking class instances."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an instance or inherited instance of a_class,
        False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
