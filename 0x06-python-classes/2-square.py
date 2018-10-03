#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=0):
        if not isinstance(size, int):
            self.size = 0
            raise TypeError("size myst be an integer")
        elif size < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.size = size
