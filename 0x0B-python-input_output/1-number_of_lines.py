#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        for i, r in enumerate(f):
            pass
        return i + 1
