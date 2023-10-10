#!/usr/bin/python3

"""
function that adds all command-line arguments to a
Python list and then saves them to a file
"""

from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    function that adds all command-line
    """
    filename = "add_item.json"
    if path.isfile(filename):
        fin_list = load_from_json_file(filename)
    else:
        fin_list = []
    for x in range(1, len(argv)):
        fin_list.append(argv[x])
    save_to_json_file(fin_list, filename)

add_items()
