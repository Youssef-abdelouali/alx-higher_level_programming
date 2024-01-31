#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class that restricts the creation of new attributes to only 'first_name'.
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
