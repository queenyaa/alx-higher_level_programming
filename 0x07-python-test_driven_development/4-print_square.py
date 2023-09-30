#!/usr/bin/python3

"""

This module is to print a Square

"""


def print_square(size):

    """
    Prints a square of '#' char with a given size

    Args:
        size (int): the size (length of one side) of the square

    Raises:
    TypeError: if 'size' is not an integer
    ValueError: if 'size' is less than 0 or a float
    """

    # check if 'size is an integer and >= 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")

    # print the square
    for _ in range(size):
        print("#" * size)
