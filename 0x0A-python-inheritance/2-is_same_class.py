#!/usr/bin/python3

""" function to check an object """


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an
    instance of a specitifed class.
    """
    return type(obj) is a_class
