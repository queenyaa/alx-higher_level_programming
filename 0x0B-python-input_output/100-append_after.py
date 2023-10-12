#!/usr/bin/python3

"""
function to insert a line of text afte each line containing a specific
string in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific
    string in a file.

    Args:
        filename (str): name of the file
        search_string (str): string to search for each line
        new_string (str): string to insert after each matching
        line
    """
    txt = ""
    with open(filename) as f:
        for lyn in f:
            txt += lyn
            if search_string in lyn:
                txt += new_string
    with open(filename, "w") as f:
        f.write(txt)
