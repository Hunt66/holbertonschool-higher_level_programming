#!/usr/bin/python3
"""THis is a rectangle class"""
class Rectangle:
    """rectangle"""

"""width property
"""
    @property
    def width(self):
        return self.__width

"""width setter
"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

"""height property
"""
    @property
    def height(self):
        return self.__height

"""height setter
"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

"""area
"""
    def area(self):
        return self.__width * self.__height

"""perimeter
"""
    def perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

"""the string of object
"""
    def __str__(self):
        str = ''
        if self.__height == 0 or self.__width == 0:
            return str
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str = str + '#'
            if i != self.__height - 1:
                str = str + '\n'
        return str

"""initialization
"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height