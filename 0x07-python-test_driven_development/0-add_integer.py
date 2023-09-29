#!/usr/bin/python3

"""

This module is to add two integers

"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    Args:
        a (int or float): the first number
        b (int or float): the second number (default is 98).

    Returns:
    int: the sum of a and b

    Raises:
    TypeError: if a or b is not an integer or float.
    """

    # Check if a and b are integers or floats, and raise an exception if not
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b into intergers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum as an int
    return (a + b)
