#!/usr/bin/python3

"""This module calculates area of the rectangle"""


class Rectangle:
    """defines the rectangle function"""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object with optional width and height

        Args:
            width (int): width of the rectangle (default to 0)
            height (int): height of the rectangle (defaults to 0)
        """

        self.width = width  # initializes width using setter method
        self.height = height  # initializes height using the setter method

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle
        Args:
            value (int): the value to set as the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle
        Args:
            value (int): the value to set as the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
