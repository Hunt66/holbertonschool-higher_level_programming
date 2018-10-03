#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if type(size) is not int:
            self.__size = 0
            raise TypeError("size myst be an integer")
        elif size < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
