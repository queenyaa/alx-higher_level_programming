#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    lgth = len(my_list)

    if idx < 0 or idx >= lgth:
        return (my_list)

    del my_list[idx]

    return (my_list)
