#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) is 0:
        return matrix
    m = [[None] * len(matrix[0])] * len(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            m[i][j] = matrix[i][j] * matrix[i][j]
    return m
