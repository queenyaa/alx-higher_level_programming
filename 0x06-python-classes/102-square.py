#!/usr/bin/python3

"""
This module prints a Square
"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (float or int): size of the square
    """
    def __init__(self, size=0):
        """
        initializes a new instance of square class

        Args:
            size (float or int, optional): size of square, defaults to 0

        Raises:
            TypeError: if size is not a number (float or int) or
                if it's negative
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            float or int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
            value (float or int): the new size of the square
        Raises:
            TypeError: if value is not a number (float or int) or
            if it's negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            float or int: the area of the square
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        checks if 2 sq instances are equal based on their areas

        Args:
            other (Square): other square instance to compare

        Returns:
            bool: true if they have the same area, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        checks if 2 sq instances are not equal based on their areas

        Args:
            other (sq): other sq instance to compare

        Returns:
            bool: true if they have different areas, false otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        checks if one sq instance is > the other based on their areas

        Args:
            other (sq): other sq instance to compare

        Returns:
            bool: true if 1st sq area is greater, false otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        checks if 1 sq instance is >= other based on their areas
        Args:
            other (sq): other sq instance to compare

        Returns:
            bool: true if the sq's area is greater, false otherwise
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        checks if 1 sq instance is < other based on area

        Args:
            other (sq): other sq instance to compare

        Returns:
            bool: true if 1st sq's area is less, false otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        checks if 1 sq instance <= to the other based on their areas

        Args:
            other (sq): other sq instance to compare

        Returns:
            bool: True if 1st sq's area is less or equal, false otherwise
        """
        return self.area() <= other.area()
