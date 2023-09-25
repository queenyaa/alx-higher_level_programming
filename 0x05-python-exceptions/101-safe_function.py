#!/usr/bin/python3

import sys


def safe_function(fct, *args):

    try:
        res = fct(*args)
        return (res)
    except Exception as j:
        print("Exception: {}".format(j), file=sys.stderr)
        return (None)
