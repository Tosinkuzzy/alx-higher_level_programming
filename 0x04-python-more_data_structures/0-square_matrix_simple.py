#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), top)) for top in matrix]
