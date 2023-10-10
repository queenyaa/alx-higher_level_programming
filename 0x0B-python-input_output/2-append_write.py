#!/usr/bin/python3

"""
function that appends a string at the end of the text file(UTF8)
returns the number of character
"""


def append_write(filename="", text=""):
    """Append a string to the end of file and return num of character"""

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
