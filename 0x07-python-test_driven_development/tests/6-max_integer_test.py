#!/usr/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Begin tests
    """

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)


    def test_positive_integers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)


    def test_negative_integers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)


    def test_mixed_integers(self):
        result = max_integer([5, -2, 0, 10, -3])
        self.assertEqual(result, 10)


    def test_duplicate_max(self):
        result = max_integer([3, 3, 3, 3, 3])
        self.assertEqual(result, 3)


    def test_max_integer_noarg(self):
        result = max_integer()
        self.assertIsNone(result)


    def test_max_integer_example(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)


    def test_max_integer_example_t(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)


    def test_max_integer_two_elements(self):
        result = max_integer([3, 4])
        self.assertEqual(result, 4)


    def test_max_integer_one_element(self):
        result = max_integer([9])
        self.assertEqual(result, 9)


    def test_max_integer_err_raised(self):
        with self.assertRaises(Exception):
            max_integer(1)
