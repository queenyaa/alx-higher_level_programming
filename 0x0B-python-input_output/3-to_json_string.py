#!/usr/bin/python3

"""
function that returns the JSON
representtaio of an object
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an obj as a string"""

    return json.dumps(my_obj)
