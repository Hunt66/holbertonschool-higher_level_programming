#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        if nb_lines < 1:
            nb_lines = 99999999999999999
        for line in (f.readlines()[0:nb_lines]):
            print(line, end="")
