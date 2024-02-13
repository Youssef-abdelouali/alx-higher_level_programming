#!/usr/bin/python3
"""Defines a function for matrix division."""


def matrix_divided(matrix, divisor):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The number by which to divide each element.
    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If the matrix contains rows of different lengths.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
