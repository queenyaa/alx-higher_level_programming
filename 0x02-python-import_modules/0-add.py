#!/usr/bin/python3

from add_0 import add
# import the add function from add_0.py
if __name__ == "__main__":
 
    # define variables a and b
    a = 1
    b = 2
    res = add(a, b)
    # Print the result
    print("{} + {} = {}".format(a, b, res))
