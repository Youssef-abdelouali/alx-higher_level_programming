#!/usr/bin/python3
"""Defines a MyInt class that inherits from int."""


class MyInt(int):
    """Defines a custom behavior for int operators == and !=."""

    def __eq__(self, value):
        """Overrides the == operator to behave like !=."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator to behave like ==."""
        return self.real == value
