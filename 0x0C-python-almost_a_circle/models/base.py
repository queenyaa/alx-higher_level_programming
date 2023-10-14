#!/usr/bin/python3

"""
Creating the "base" class which will serve as the foundatoin
for other classes
"""
import json


class Base:
    """
    Class to serve as the foundation
    for other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        # if id is provided, set it as a public instance attribute
        if id is not None:
            self.id = id
        else:
            """
            if id is not provided, increment __nb_objects and assign
            it to the id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of
        list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dictionaries)
            file.write(json_str)
