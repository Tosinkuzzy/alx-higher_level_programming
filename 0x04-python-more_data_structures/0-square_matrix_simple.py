#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    new _matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix)):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    return new_matrix
