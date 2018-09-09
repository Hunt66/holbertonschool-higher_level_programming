#!/usr/bin/python3
def pow(a, b):
    d = 1
    if b < 0:
        b = abs(b)
        for c in range(b):
            d = d / a
    else:
        for c in range(b):
            d = d * a
    return d
