#!/usr/bin/python3

"""
Class that inherits from the Rectangle class and have a constructor
that accepts the size, x, y and id attributes
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that have a constructor that accpets
    size, x, y and id
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.with

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute, assigns the same value
        to width and height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square
        instance
        """
        divi = f"{self.x}/{self.y}"
        return (f"[Square] ({self.id}) {divi} - {self.width}")
