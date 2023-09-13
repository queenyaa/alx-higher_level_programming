#!/usr/bin/python3


def uniq_add(my_list=[]):

    uniq_set = set()

    for n in my_list:
        uniq_set.add(n)

    res = sum(uniq_set)

    return (res)
