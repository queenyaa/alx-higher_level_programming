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
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute, assigns the same value
        to width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign attributes to the instance using both
        non-keyworded and keyworded arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """
        Return a string representation of the square
        instance
        """
        divi = f"{self.x}/{self.y}"
        return (f"[Square] ({self.id}) {divi} - {self.width}")

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
