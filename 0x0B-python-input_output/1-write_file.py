#!/usr/bin/python3

"""
function that writes a string
to a text file and returns the number of characters
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number"""

    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
