#!/usr/bin/python3

"""
class that a child class, MyList inherits
from
"""


class MyList(list):
    def print_sorted(self):
        """Prints the list in sorted, ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
