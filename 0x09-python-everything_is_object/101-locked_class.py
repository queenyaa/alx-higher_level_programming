#!/usr/bin/python3

"""
This module defines a class that prevent the dynamic
creation of new instance attributes
"""


class LockedClass:
    """class defined to prevent dynamic creation"""
    __slots__ = ["first_name"]
