#!/usr/bin/python3

""" this module prints a string n times """


def magic_string():
    """function to print strings n times"""

    if not hasattr(magic_string, "count"):
        magic_string.count = 1
    else:
        magic_string.count += 1
    return ("BestSchool" + (", BestSchool" * (magic_string.count - 1)))
