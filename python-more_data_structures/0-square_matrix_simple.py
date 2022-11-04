#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return [[number * number for number in row] for row in matrix]
