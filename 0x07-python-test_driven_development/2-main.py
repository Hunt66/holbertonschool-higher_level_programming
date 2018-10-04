#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[1,2,3],[1,None, 6]]

try:
    print(matrix_divided(matrix, "str"))
except Exception as e:
    print(e)
print(matrix)
