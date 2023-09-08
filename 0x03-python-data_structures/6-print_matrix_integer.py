#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:

        for t, v in enumerate(row):
            if t < len(row) - 1:
                print("{:d} ".format(v), end="")
            else:
                print("{:d}".format(v), end="")
        print()
