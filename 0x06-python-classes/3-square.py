#!/usr/bin/python3

"""
This modules defines a square class
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the square class.

        Args:
            size (int, optional): The size of the square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: the area of the square.
        """
        return (self.__size ** 2)
