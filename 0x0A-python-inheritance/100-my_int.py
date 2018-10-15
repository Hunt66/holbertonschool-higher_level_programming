#!/usr/bin/python3
class MyInt(int):

    def __init__(self, value):
        self._Int__value = value

    def __eq__(self, other):
        if self._Int__value == other:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
