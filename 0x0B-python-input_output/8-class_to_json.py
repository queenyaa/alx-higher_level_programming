#!/usr/bin/python3

"""
functino that returns a dictionary description with simple
data structures fro JSON serialization of an object
"""


def class_to_json(obj):
    """Return to dictionary representation of a class instance"""

    n_dict = {}
    for key, value in obj.__dict__.items():
        if key.startswith('_' + obj.__class__.__name__ + '__'):
            n_key = key[1 + len(obj.__class__.__name__):]
            n_dict[n_key] = value
        else:
            n_dict[key] = value

    return n_dict
