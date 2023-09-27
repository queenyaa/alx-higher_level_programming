#!/usr/bin/python3

"""
write an info of Python
"""

import math


class MagicClass:
    """
    A class that represents a magic circle with radius and provides methods
        to calculates area and circumference.

    Attributes:
        __radius (float or int): the radius of the magic circle

    Methods:
        __init__(self, radius=0): Initializes a MagicClass instance with
            a given radius.
        area(self): calculates and returns the area of the magic circle
        circumference(self): calculates and returns the circumference of the
            magic circle
    """

    def __init__(self, radius=0):
        """
        initializes a new instance of the MagicClass class with given radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle

        Returns:
            float: area of the magic circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        calculates and returns the circumference of the magice circle

        Returns:
            float: circumference of the magic circle
        """
        return 2 * math.pi * self.__radius
