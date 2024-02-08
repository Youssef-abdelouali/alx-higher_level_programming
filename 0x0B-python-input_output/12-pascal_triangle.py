#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tri_Angle = [[1]]
    while len(tri_Angle) != n:
        tri_an = tri_Angle[-1]
        temp_r = [1]
        for i in range(len(tri_an) - 1):
            temp_r.append(tri_an[i] + tri_an[i + 1])
        temp_r.append(1)
        tri_Angle.append(temp_r)
    return tri_Angle
