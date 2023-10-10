#!/usr/bin/python3

"""
class to define a student with specified attributes and a to_json
method to retrieve a dictionary representation of a student instance
"""


class Student:
    """class the defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance with first_name, last_name"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict representation of a student instance"""
        
        if attrs is None:
            return self.__dict__

        res = {}
        for attr in attrs:
            if hasattr(self, attr):
                res[attr] = getattr(self, attr)
        return res
