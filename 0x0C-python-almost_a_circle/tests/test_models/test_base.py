#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
"""
import os
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSaveToFileMethod(unittest.TestCase):

    def test_save_to_file_with_valid_data(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        filename = "Rectangle.json"

        Base.save_to_file(list_rectangles)

        with open(filename, "r") as file:
            data = file.read()
            self.assertIsInstance(data, str)
            self.assertNotEqual(data, "")

        os.remove(filename)

    def test_save_to_file_with_empty_data(self):
        list_rectangle = []
        filename = "Rectangle.json"

        Base.save_to_file(list_rectangles)

        with open(filename, "r") as file:
            data = file.read()
            self.assertIsInstance(data, str)
            self.assertEqual(data, "")

        os.remove(filename)

    def test_save_to_file_with_none_data(self):
        list_rectangles = None
        filename = "Rectangle.json"

        Base.save_to_file(list_rectangles)

        with open(filename, "r") as file:
            data = file.read()
            self.assertIsInstance(data, str)
            self.assertEqual(data, "")

        os.remove(filename)


class TestCreateMethod(unittest.TestCase):

    def test_create_rectangle(self):
        rectangle_dict = {
                'id': 1,
                'width': 5,
                'height': 10,
                'x': 2,
                'y': 3
        }
        result = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(result, Rectangle)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 5)
        self.assertEqual(result.height, 10)
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 3)

    def test_create_square(self):
        square_dict = {
                'id': 2,
                'size': 7,
                'x': 1,
                'y': 4
        }
        result = Square.create(**square_dict)
        self.assertIsInstance(result, Square)
        self.assertEqual(result.id, 2)
        self.assertEqual(result.size, 7)
        self.assertEqual(result.x, 1)
        self.assertEqual(result.y, 4)

    def test_invalid_class_name(self):
        invalid_dict = {
                'id': 3,
                'name': 'InvalidClass',
                'value': 42
        }
        result = Base.create(**invalid_dict)
        self.assertIsNone(result)


class TestFromJsonStringMethod(unittest.TestCase):

    def test_from_json_string_with_valid_json(self):
        json_string = '[{"id": 1, "name": "item1"}, {"id": 2, "item2"}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], {"id": 1, "name": "item1"})
        self.assertEqual(result[1], {"id": 2, "name": "item2"})

    def test_from_json_string_with_empty_json(self):
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_from_json_string_with_none_json(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)


class TestLoadFromFile(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_from_file_existing_file(self):
        # Create a sample JSON file with data
        data = '[{"id": 1, "name": "Object 1"}, {"id": 2, "name": "Object 2"}]'
        with open("Base.json", "w") as file:
            file.write(data)

        # Load data from the file using load_from_file
        instances = Base.load_from_file()

        # Check if the loaded data matches the expected result
        self.assertEqual(len(instances), 2)

    def test_load_from_file_nonexistent_file(sef):
        # Attempt to load data from a non-extistent file
        instances = Base.load_from_file()

        # Check if the result is an empty list
        self.assertEqual(len(instances), 0)


class TestCSVMethods(unittest.TestCase):

    def setUp(self):
        # Optional: Prepare any data or setup needed for the test
        pass

    def tearDown(self):
        # Optional: clean up after the tests
        pass

    def test_save_to_file_csv(self):
        # create instances or data to be saved to CSV
        rect1 = Rectangle(4, 6)
        rect2 = Rectangle(3, 3)
        square1 = Square(5)
        square2 = Square(2)

        # save the data to a CSV file using save_to_file_csv
        Rectangle.save_to_file_csv([rect1, rect2])
        Square.save_to_file_csv([square1, square2])

    def test_load_from_file_csv(self):
        # load data from the CSV file using load_from_file_csv
        rectangles = Rectangle.load_from_file_csv()
        squares = Square.load_from_file_csv()

        # perform assertions to check if the loaded data is as expected
        self.assertIsInstance(rectangles, list)
        self.assertIsInstance(squares, list)


class TestBaseDraw(unittest.TestCase):

    @patch('turtle.Turtle')
    @patch('turtle.Screen')
    @patch('turtle.mainloop')
    def test_draw(self, mock_mainloop, mock_screen, mock_turtle):

        r1 = Rectangle(100, 40)
        r2 = Rectangle(90, 110, 30, 10)
        r3 = Rectangle(20, 25, 110, 80)
        s1 = Square(35)
        s2 = Square(15, 70, 50)
        s3 = Square(80, 30, 70)

        list_rectangles = [r1, r2, r3]
        list_squares = [s1, s2, s3]

        Base.draw(list_rectangles, list_squares)

        self.assertTrue(mock_mainloop.called)
        self.assertTrue(mock_screen.called)
        self.assertTrue(mock_turtle.called)


if __name__ == '__main__':
    unittest.main()
