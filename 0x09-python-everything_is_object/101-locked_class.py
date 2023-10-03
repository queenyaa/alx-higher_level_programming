#!/usr/bin/python3

"""
This module defines a class that prevent the dynamic
creation of new instance attributes
"""


class LockedClass:
    """class that prevents the dynamic creation of new instances attributes"""

    __slots__ = ["first_name"]
"""
    def __init__(self, first_name):
        self.first_name = first_name
"""
