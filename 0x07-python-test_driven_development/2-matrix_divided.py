#!/usr/bin/python3
def matrix_divided(matrix, div):
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    out = []
    for i in range(0, len(matrix)):
        out1 = []
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, len(matrix[i])):
            if matrix[i][j] is None or (not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            out1.append(round(matrix[i][j] / div, 2))
        out.append(out1)
    return out
