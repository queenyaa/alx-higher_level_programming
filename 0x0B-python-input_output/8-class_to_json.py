#!/usr/bin/python3

"""
functino that returns a dictionary description with simple
data structures fro JSON serialization of an object
"""


def class_to_json(obj):
    """Return to dictionary representation of a class instance"""

    # obj_dict = obj.__dict__.copy()  # copy the instance dictionary

    # handle private attributes with name mangling
    n_dict = {}
    for key, value in obj.__dict__.items():
        if key.startswith('_' + obj.__class__.__name__ + '__'):
            n_key = key[1 + len(obj.__class__.__name__):]
            # obj_dict[n_key] = obj_dict.pop(key)
            n_dict[n_key] = value
        else:
            n_dict[key] = value

    return n_dict
