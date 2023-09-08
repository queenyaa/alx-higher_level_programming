#!/usr/bin/python3
from sys import argv
argx = len(argv) - 1


def sum_arg():

    tot = 0
    for v in range(1, len(argv)):
        tot += int(argv[v])
    return tot


if __name__ == "__main__":
    if (argx == 0):
        print("{:d}".format(argx))
    else:
        print("{:d}".format(sum_arg()))
