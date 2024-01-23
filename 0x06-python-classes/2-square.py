#!/usr/bin/python3

class Square:
    """Represent a class square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
