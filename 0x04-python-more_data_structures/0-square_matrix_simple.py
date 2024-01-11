#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), lm)) for lm in matrix]
