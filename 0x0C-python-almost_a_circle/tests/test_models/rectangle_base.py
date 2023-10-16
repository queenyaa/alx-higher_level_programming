#!/usr/bin/python3
"""Defines unittests for rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestRectangle(unittest.TestCase):
    
    def test_init(self):
        r = Rectangle(5, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(3, 2, 2, 3, 7)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_str(self):
        r = Rectangle(5, 4, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 5/4")
        r = Rectangle(10, 7, 0, 0, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 10/7")

    def test_area(self):
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(4, 3, 1, 1)
        self.assertEqual(r.display(), "\n ####\n ####\n ####")
        r = Rectangle(2, 2, 2, 2)
        self.assertEqual(r.display(), "\n\n  ##\n  ##")

    def test_update(self):
        r = Rectangle(5, 4, 1, 1, 1)
        r.update(7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/1 - 5/4")
        r.update(8, 2)
        self.assertEqual(str(r), "[Rectangle] (8) 1/1 - 2/4")
        r.update(9, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (9) 1/1 - 2/2")
        r.update(10, 2, 2, 0)
        self.assertEqual(str(r), "[Rectangle] (10) 0/1 - 2/2")
        r.update(11, 2, 2, 0, 0)
        self.assertEqual(str(r), "[Rectangle] (11) 0/0 - 2/2")

    def test_update_kwargs(self):
        r = Rectangle(5, 4, 1, 1, 1)
        r.update(id=7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/1 - 5/4")
        r.update(id=8, width=2)
        self.assertEqual(str(r), "[Rectangle] (8) 1/1 - 2/4")
        r.update(id=9, width=2, height=2)
        self.assertEqual(str(r), "[Rectangle] (9) 1/1 - 2/2")
        r.update(id=10, width=2, height=2, x=0)
        self.assertEqual(str(r), "[Rectangle] (10) 0/1 - 2/2")
        r.update(id=11, width=2, height=2, x=0, y=0)
        self.assertEqual(str(r), "[Rectangle] (11) 0/0 - 2/2")


if __name__ == '__main__':
    unittest.main()
