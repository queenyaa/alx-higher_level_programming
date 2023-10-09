#!/usr/bin/python3

"""
class to define area of a rectangle
"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Calculate the area. This method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): name of the value (always a string).
            value: value to be validated

        Raises:
            TypeError: the value is not an integer
            ValueError: the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle instance with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
