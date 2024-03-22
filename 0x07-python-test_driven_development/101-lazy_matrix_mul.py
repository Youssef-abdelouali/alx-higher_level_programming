#!/usr/bin/python3
"""Implements a matrix multiplication function using NumPy."""
import numpy as numpy


def lazy_matrix_mul(m_a, m_b):
    """Calculates the product of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
        
    Returns:
        Array: Resultant matrix obtained from the multiplication.
    """

    return numpy.matmul(m_a, m_b)
