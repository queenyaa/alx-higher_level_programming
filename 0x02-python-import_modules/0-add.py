#!/usr/bin/python3

# import the add function from add_0.py
# if __name__ == "__main__":

from add_0 import add

# define variables a and b
a = 1
b = 2
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
