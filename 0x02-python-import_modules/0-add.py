#!/usr/bin/python3

#import the add function from add_0.py
if __name__ == "__main__":
    """Print the sum of 1 and 2"""
    from add_0 import add
    # define variables a and b
    a = 1
    b = 2

    # Print the result
    print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
