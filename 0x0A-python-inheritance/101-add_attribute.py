#!/usr/bin/python3


"""function to add a new attribute"""


def add_attribute(obj, attr, value):
    """ function to add a new attribute"""

    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)

    else:
        raise TypeError("can't add new attribute")
