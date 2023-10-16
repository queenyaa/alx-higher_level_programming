#!/usr/bin/python3

"""Defines unittests for square.py.

Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import os
import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSqaure(unittest.TestCase):

    def test_init(self):
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(3, 2, 3, 7)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")
        s = Square(10, 0, 0, 2)
        self.assertEqual(str(s), "[Square} (2) 0/0 - 10")

    def test_update_args(self):
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s.update(20, 30)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s.update(30, 40, 50)
        self.assertEqual(s.id, 30)
        self.assertEqual(s.size, 40)
        self.assertEqual(s.x, 50)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(5, 2, 3, 1)
        s.update(id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s.update(size=20, x=30)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 30)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


    def test_size_property(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_str_method(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_update_method(self):
        s = Square(5, 2, 3, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.update(10, 20)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 20")
        s.update(10, 20, 30)
        self.assertEqual(str(s), "[Square] (10) 20/3 - 30")
        s.update(10, 20, 30, 40)
        self.assertEqual(str(s), "[Square] (10) 20/40 - 30")
        s.update(id=5, size=15)
        self.assertEqual(str(s), "[Square] (5) 20/40 - 15")
        s.update(id=5, x=1, y=2)
        self.assertEqual(str(s), "[Square] (5) 1/2 - 15")


if __name__ == '__main__':
    unittest.main()
