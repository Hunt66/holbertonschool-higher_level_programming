#!/usr/bin/python3
"""THis is a rectangle class
"""
class Rectangle:
    """rectangle
    """

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

"""area of rect
"""
    def area(self):
        return self.__width * self.__height

"""perimeter
"""
    def perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

"""initialization
"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
