#!/usr/bin/python3

"""
functino that returns a Python data
structure represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Return a Python data structure from a JSON string"""

    return json.loads(my_str)
