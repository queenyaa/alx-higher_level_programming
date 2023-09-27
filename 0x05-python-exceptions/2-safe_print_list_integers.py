#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    cnt = 0

    for d in range(x):
        try:
            # for d in range(x):
            # if isinstance(my_list[d], int):  # check if item is an int
            print("{:d}".format(my_list[d]), end="")
            cnt += 1
        except (TypeError, ValueError):
            pass

    print()  # print a newline char to separate the output
    return (cnt)  # return the real num of int printed
