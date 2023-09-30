#!/usr/bin/python3

"""

This module is to print text with 2 new line after '.',
'?' and ':'
"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each '.', '?' and ':' characters

    Args:
        text (str): the input text

    Raises:
    TypeError: if 'text' is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    lyn = ""

    # iterate through each character in the input text
    for char in text:
        # if the char is '.', '?' or ':' print line and reset it
        if char in '.?:':
            lyn += char  # add the char
            # print(lyn)
            print(lyn.strip())  # Remove leading/trailing spaces
            print()  # print two new lines
            lyn = ""
            # lyn = "."  # add a period
            # lyn += "\n\n"  # add two new lines
        else:
            lyn += char  # append the char to the current line

    # print the last line if not empty
    if lyn:
        print(lyn.strip(), end="")  # remove leading/trailing spaces
        # print(lyn)
