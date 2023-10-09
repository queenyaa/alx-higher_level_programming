#!/usr/bin/python3

"""
class with area method that raises
an exception
"""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Calculate the area. This method raises an exception."""
        raise Exception("area() is implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): the name of the value (always a string)
            value: value to be validated

        Raises:
            TypeError: the value is not an integer
            ValueError: value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
