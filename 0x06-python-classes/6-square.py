#!/usr/bin/python3

"""
this module defines the square class
"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): the size of the square
        __position (tuple): the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the square class

        Args:
            size (int, optional): size of the square, defaults to 0
            position (tuple, optional) the position of the square,
                defaults to (0, 0)

        Raises:
            TypeError: if size is not an integer or if position is not a tuple
                of two positive integers
            ValueError: if size is less than 0 or if position contains non-
                positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(x, int) for x in position) or \
                not all(x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        args:
            value (int): new size of square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        slef.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square

        Returns:
            tuple: the position of the square as a tuple of two positive
                integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square

        Args:
            value (tuple): the new position of the square as a tuple of two
                positive integers.
        Raises:
            TypeError: if value is not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(x, int) for x in value) or \
                not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of two positive \
                    integers")
        self.__position = value

    def area(self):
        """
        calculates and returns the area of the square

        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints the square using '#' char and positioning

        if size = 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
