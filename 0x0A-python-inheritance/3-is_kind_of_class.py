#!/usr/bin/python3

""" Class to check an object is an instance"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance of, or if the object is
    an instance of a class that inherited form, the specified class.

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        Bool: True if obj is an instance of a_class or its subclass,
            False otherwise
    """
    return isinstance(obj, a_class)
