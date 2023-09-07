#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        d = add(a, b)
        for v in range(4, 6):
            d = add(d, v)
        return (d)
    else:
        return (sub(a, b))
