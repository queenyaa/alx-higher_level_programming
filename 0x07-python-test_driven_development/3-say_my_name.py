#!/usr/bin/python3

"""

This module is to print full name

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the given fist and last name

    Args:
        first_name (str): first name to be printed
        last_name (str, optional): last name to be printed

    Raises:
    TypeError: If 'first_name' or 'last_name' is not string
    """
    # check if first name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
