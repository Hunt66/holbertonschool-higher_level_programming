#!/usr/bin/python3
class Rectangle:

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

    def __str__(self):
        strr = ''
        if self.__height == 0 or self.__width == 0:
            return strr
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                strr = strr + '#'
            if i != self.__height - 1:
                strr = strr + '\n'
        return strr

    def __repr__(self):
        strr = "Rectangle("
        width = self.__width
        strr += str(width)
        strr += ', '
        height = self.__height
        strr += str(height)
        strr += ')'
        return strr

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
