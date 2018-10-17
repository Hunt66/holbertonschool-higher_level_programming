#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return [[]]
    current = [1]
    new = []
    ret = [[]]
    for i in range(0, n):
        ret += [current]
        for j in range(0, len(current) + 1):
            if j == 0:
                new += [1]
            elif j == len(current):
                new += [1]
            else:
                new += [(current[j] + current[j - 1])]
        current = new.copy()
        new = []
    return(ret)
