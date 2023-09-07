#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        calculate(a, operator, b)

if operator == '+':
    print("{:d} {} {:d}".format(a, operator, b, add(a, b)))
elif operator == '-':
    print("{:d} {} {:d}".format(a, operator, b, sub(a, b)))
elif operator == '*':
    print("{:d} {} {:d}".format(a, operator, b, mul(a, b)))
elif operator == '/':
    print("{:d} {} {:d}".format(a, operator, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
