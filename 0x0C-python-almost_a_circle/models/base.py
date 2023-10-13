#!/usr/bin/python3

"""
Creating the "base" class which will serve as the foundatoin
for other classes
"""


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
