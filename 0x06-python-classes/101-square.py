#!/usr/bin/python3
class Square:
    __size = 0
    position = (0, 0)
    def __init__(self, new_size=0, new_position=(0,0)):   # initialization
        if not isinstance(new_position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_position[0], int) or new_position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_position[1], int) or new_position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(new_size, int):
            self.size = 0
            raise TypeError("size myst be an integer")
        elif new_size < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.size = new_size
            self.position = new_position
    def position(self, value):            # position setter
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value
    def position(self):                    #position retriever
        return self.position
    def size(self, value):                 #size setter
        if not isinstance(value, int):
            self.size = 0
            raise TypeError("size myst be an integer")
            exit
        elif value < 0:
            self.size = 0
            raise ValueError("size must be >= 0")
        else:
            self.size = value
    def size(self):                       #size getter
        return self.size
    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size myst be an integer")
        return (self.size * self.size)
    def my_print(self):                        #print square
        for i in range(0, self.size):
            for i in range(0, self.position[0]):
                print(' ', end='')
            for i in range(0, self.size):
                print('#', end='')
            print('')
        if self.size == 0:
            print('')
