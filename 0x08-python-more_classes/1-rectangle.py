#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access or modify the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rect,ensuring it is an int and n-negative."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self.__width = value

    @property
    def height(self):
        """Access or modify the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rect,ensuring it is an int and n-negative."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self.__height = value
