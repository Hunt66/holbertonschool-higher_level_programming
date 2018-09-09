#!/usr/bin/python3

#This function checks if a letter is lowercase returns True if it is

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
