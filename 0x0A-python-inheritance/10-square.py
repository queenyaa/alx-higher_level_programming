#!/usr/bin/python3

"""
Square calculation
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to calculate square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
