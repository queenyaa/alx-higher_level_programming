#!/usr/bin/python3

"""
Function to check if an object is an instance of a class
was inherted
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: the object to check
        a_class: class to compare against

    Return:
        bool: True if obj is an instance of a subclass of a_class
            False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
