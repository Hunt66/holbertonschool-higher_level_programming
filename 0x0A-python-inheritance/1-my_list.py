#!/usr/bin/python3
class MyList():
    __list = []

    def append(self, num):
        MyList.__list += [num]

    def print_sorted(self):
        nlist = self.__list.copy()
        nlist.sort()
        print(nlist)

    def __str__(self):
        return str(self.__list)
