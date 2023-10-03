#!/usr/bin/python3

"""Class to define rectangle"""


class Rectangle:
    """function to define rectangle and return a string representation"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        """
        Returns a str representation of the rectangle with '#'
        if width or height = 0, an empty str is returned
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a str representation of the rectangle for recreating an
        instance
        """
        return (f"Rectangle({self.__width}, {self.__height})")
