#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        best_key = ""
        best_val = float('-inf')

        for key, value in a_dictionary.items():
            if value > best_val:
                best_key = key
                best_val = value

        return (best_key)
    else:
        return (None)
