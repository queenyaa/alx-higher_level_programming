#!/usr/bin/python3

"""
This module defines the class rectangle
"""


class Rectangle:
    """
    class that defines a Rectangle and prints a message when an instance
    is deleted
    """
    number_of_instances = 0  # Class attribute initialized to 0

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # increment the class attribute

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

        return self._height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):

        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
