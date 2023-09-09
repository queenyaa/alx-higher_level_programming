#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:

        return (None)

    max_v = my_list[0]

    for v in my_list:
        if v > max_v:
            max_v = v

    return (max_v)
