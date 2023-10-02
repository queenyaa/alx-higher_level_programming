#!/usr/bin/python3

"""This module defines the Rectangle class"""


class Rectangle:
    """
    class the defines a rectangle and adds new instance and
    decreases it upon deletion
    """
    number_of_instances = 0
    print_symbol = "#"  # class attribute for symbol for string representation

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""

        rec = []
        for x in range(self.__height):
            [rec.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                rec.append("\n")
        # return '\n'.join([str(self.print_symbol) * self.__width])
        return "".join(rec)

    def __repr__(self):

        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
