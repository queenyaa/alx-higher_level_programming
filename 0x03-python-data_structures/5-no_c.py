#!/usr/bin/python3


def no_c(my_string):
    n_str = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            n_str += char
    return (n_str)
