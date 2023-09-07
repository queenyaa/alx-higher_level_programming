#!/usr/bin/python3

from sys import argv
arg_0 = "arguments."
arg_1 = "argument:"
arg_n = "arguments:"
argc = len(argv) - 1

def print_args():
    for v in range(1, len(argv)):
        print("{:d}: {}".format(v, argv[v]))

if __name__ == "__main__":
    if (argc == 0):
        print("{:d} {}".format(argc, arg_0))
    elif (argc == 1):
        print("{:d} {}".format(argc, arg_1))
        print_args()
    else:
        print("{:d} {}".format(argc, arg_n))
        print_args()

#if __name__ == "__main__":
    #import sys

    #num_args = len(sys.argv) - 1

    #print("{} argument{}{}:".format(num_args, 's' if num_args != 1
        #else '', 's' if num_args != 1 else '.' if num_args == 0 else ':'))

    #for v in range(1, len(sys.argv)):
        #print("{}: {}".format(v, sys.argv[v]))
