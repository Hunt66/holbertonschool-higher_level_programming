#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in range(0, self.__y):
            print('')
        for i in range(0, self.__height):
            for j in range(0, self.__x):
                print(' ', end='')
            for j in range(0, self.__width):
                print('#', end='')
            if i != self.__height:
                print('')

    def __str__(self):
        st = "[Rectangle] (" + str(self.id) + ') ' + str(self.__x) + '/'
        st += str(self.__y)
        st += " - " + str(self.__width) + '/' + str(self.__height)
        return st

    def update(self, *args, **kwargs):
        if (args) and args != ():
            if len(args) >= 1:
                super(Rectangle, self).__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    super(Rectangle, self).__init__(v)
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v


    def to_dictionary(self):
        return self.__dict__

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.width = width
        self.x = x
        self.y = y
        self.height = height
