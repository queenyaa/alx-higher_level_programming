#!/usr/bin/python3

"""
class that defines a student with specified attributes
and a method to retrive a dictionary representation
"""


class Student:
    """calls to define a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a studnet instance with first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a student instance"""
        return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
        }
