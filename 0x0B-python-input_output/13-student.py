#!/usr/bin/python3
class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        ret = {}
        for i, r in self.__dict__.items():
            if i in attrs:
                ret[i] = r
        return ret

    def reload_from_json(self, json):
        for i, j in json.items():
            self.__dict__[i] = j
