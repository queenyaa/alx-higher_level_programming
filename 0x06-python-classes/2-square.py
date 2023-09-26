#!/usr/bin/python3

"""
This module defines the square class.
"""


class Square:
    """
    This is the square class.

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of square class

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
