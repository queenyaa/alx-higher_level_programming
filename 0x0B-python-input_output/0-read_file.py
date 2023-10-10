#!/usr/bin/python3

"""function to read and print
contents to stdout
"""


def read_file(filename=""):
    """Read and print the contents of a text file to stdout."""

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
