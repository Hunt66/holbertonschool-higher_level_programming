#!/usr/bin/python3

def uppercase(str):
    islower = __import__('7-islower').islower
    i = 0
    for c in str:
        if islower(c) == False:
            i = ord(c - 32)
            c = chr(i)
        print("{:s}" .format(c), end='')
    print("")
