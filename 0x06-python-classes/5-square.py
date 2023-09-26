#!/usr/bin/python3


"""
This module defines a square class
"""


class Square:
    """
    This clas represents a square.

    Attributes:
        __size (int): the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class

        Arg:
            size (int, optional): the size of the square, defaults to 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): the new size the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area

        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square using '#' char.

        if the size is equal to 0, print empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
