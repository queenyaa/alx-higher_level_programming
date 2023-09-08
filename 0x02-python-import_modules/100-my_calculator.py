#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    opera = argv[2]
    g = {"+": add, "-": sub, "*": mul, "/": div}

    if opera not in g:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, opera, b, g[opera](a, b)))

# if operator == '+':
    # print("{:d} {} {:d}".format(a, operator, b, add(a, b)))
# elif operator == '-':
    # print("{:d} {} {:d}".format(a, operator, b, sub(a, b)))
# elif operator == '*':
    # print("{:d} {} {:d}".format(a, operator, b, mul(a, b)))
# elif operator == '/':
    # print("{:d} {} {:d}".format(a, operator, b, div(a, b)))
# else:
    # print("Unknown operator. Available operators: +, -, * and /")
    # exit(1)#
