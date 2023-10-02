#!/usr/bin/python3

"""

Module to define Rectangle
"""


class Rectangle:
    """Represents a rectangle"""


    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): height of the rectangle (default is 0).
        """
        self.width = width  # Initializes width using the setter method
        self.height = height  # Initializes height using the setter method

    @property
    def width(self):
        """
        Getting method for retrieving the width
        of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle

        Args:
            value (int): the value to set as the width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        setter method for setting the height
        of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle

        Args:
            value (int): value to set as the height

        Raises:
            TypeError: if value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
