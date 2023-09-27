#!/usr/bin/python3

"""
this module defines the square class
"""


class Square:
    """
    this class represents a square

    Attributes:
        __size (int): size of the square
        __position (tuple): position of the square
    """

    def __str__(self):
        """
        Returns a string representation of the  suare for printing
            a square

        Returns:
            str: string representation of the square
        """
        return self.myn_print()

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class

        Args:
            size (int, optional): the size of the square, defaults to 0
            position (tuple, optional): the position ofthe square, defaults
                to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the sixe of the square.

        Args:
            value (int): the new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
        Sets the position of the square

        Args:
            value (tuple): the new position the square as a tuple of two
                positive integers

        Raises:
            TypeError: if value is not a tuple of two positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates the area of the square

        returns:
            int: the are of the square.
        """
        return (self.__size ** 2)

    def myn_print(self):
        """
        Prints a square with '#' chars and positioning

        if the size is equal to 0, it prints an empty line
        position is used to add spaces before printing the square
        """

        myn = ""

        if self.size == 0:
            return myn

        for x in range(self.position[1]):
            myn += "\n"
        for x in range(0, self.size):
            for v in range(self.position[0]):
                myn += " "
            for y in range(self.size):
                myn += "#"
            if x is not (self.size - 1):
                myn += "\n"
        return myn

    def my_print(self):
        """
        Print square
        """
        if self.size == 0:
            print()
        else:
            for x in range(self.postion[1]):
                print()
            for x in range(0, self.size):
                for v in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.size):
                    print("#", end="")
                print()
