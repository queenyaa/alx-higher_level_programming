#!/usr/bin/python3

"""
class that defines a student with the specified attributes and includes
the methods to_json and reload_from_json for serialization and
deserialization
"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance with first_name, last_name"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dict representation of a student instance
        with optional attribute filtering.
        """

        if attrs is None:
            return self.__dict__

        res = {}
        for attr in attrs:
            if hasattr(self, attr):
                res[attr] = getattr(self, attr)
        return res

    def reload_from_json(self, json):
        """
        Replace all attributes of the student instance with values
        from a dictionary.
        """

        for key, value in json.items():
            setattr(self, key, value)
