#!/usr/bin/python3
import json

class Base():
    __nb_objects = 0

    def save_to_file(cls, list_objs):
        filename = str(cls) + '.json'
        with open(filename, 'r+') as f:
            f.seek(0)
            

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
