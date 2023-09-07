#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1

    print("{} argument{}{}:".format(num_args, 's' if num_args != 1
        else '', 's' if num_args != 1 else '.' if num_args == 0 else ':'))

    for v in range(1, len(sys.argv)):
        print("{}: {}".format(v, sys.argv[v]))
