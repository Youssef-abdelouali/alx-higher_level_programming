#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squar_matr = []
    for i in matrix:
        squar_matr.append([j**2 for j in i])
    return squar_matr
