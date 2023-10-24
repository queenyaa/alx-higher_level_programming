#!/usr/bin/python3
"""
Unittesting for base.py
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class Testing_Base(unittest.TestCase):
    """Defines a class to evaluate different cases"""

    def test_instance_type_class_id(self):
        """ check instance of class """
        d1 = Base()
        self.assertIsInstance(d1, Base)
        self.assertFalse(type(d1) == type(Base))
        self.assertFalse(id(d1) == id(Base))
        d2 = Base()
        self.assertTrue(type(d1) == type(d2))
        self.assertFalse(id(d1) == id(d2))

    def test_id_none(self):
        """Checks for id being none """
        d1 = Base()
        self.assertEqual(d1.id, 1)
        d1 = Base()
        self.assertEqual(d1.id, 2)
        d1 = Base()
        self.assertEqual(d1.id, 3)
        d2 = Base()
        self.assertEqual(d2.id, 4)

    def test_id_value(self):
        """Checks when id has a integer value """
        d1 = Base(12)
        self.assertEqual(d1.id, 12)
        d1.id = 4
        self.assertEqual(d1.id, 4)
        d2 = Base(50)
        self.assertEqual(d2.id, 50)
        d1 = Base(-4)
        self.assertEqual(d1.id, -4)
        d2 = Base(0)
        self.assertEqual(d2.id, 0)
        d1 = Base(100e+1000)
        self.assertEqual(d1.id, 100e+1000)
        d1.__init__(30)
        self.assertEqual(d1.id, 30)

    def test_attributes_obj(self):
        """ Check for dictionary attributes as an object"""
        d1 = Base()
        self.assertEqual(d1.__dict__, {'id': 1})
        d2 = Base()
        self.assertEqual(d2.__dict__, {'id': 2})
        d3 = Base(100)
        self.assertEqual(b3.__dict__, {'id': 100})

    def test_errors_raise(self):
        """Check for errors"""
        with self.assertRaises(AttributeError):
            d1 = Base()
            print(d1.x)
        with self.assertRaises(NameError):
            d1 = Base_geometry()
        with self.assertRaises(AttributeError):
            d1.to_dictionary()

    def test_JSON_string(self):
        """ Check for json string method """
        t1 = Rectangle(10, 7, 2, 8)
        dictionary = (t1.to_dictionary())
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 1], '
                        '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        t2 = Rectangle(10, 7, 2, 8, 30)
        dictionary = t2.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 2], '
                        '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        t3 = Rectangle(30, 50)
        dictionary = t3.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_ditionary, '[["height", 7], ["id", 3], '
                        '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        t5 = Rectangle(30, 50, 0, 0, 89)
        dictionary = t5.to_dictionary()
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_ditionary, '[["height", 7], ["id", 89], '
                        '["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        dictionary = None
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')
        self.assertTrue(type(dictionary) != type(json_dictionary))

    def test_save_to_file(self):
        """ Checks to save to file """
        t1 = Rectangle(10, 7, 2, 8)
        t2 = Rectangle(2, 4)
        Rectangle.save_to_file([t1, t2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lamdba x: ord(x), '[{"y": 8, "x": 2, '
                                    '"id": 1, "width": 10, "height": 7}, '
                                    '{"y": 0, "x": 0, "id": 2, '
                                    '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        t1 = Rectangle(10, 7)
        t2 = Rectangle(2, 4)
        Rectangle.save_to_file([t1, t2])
        with open("Rectangle.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lamdba x: ord(x), '[{"y": 0, "x": 0, '
                                        '"id": 3, "width": 10, "height": 7}, '
                                        '{"y": 0, "x": 0, "id": 4, '
                                        '"width": 2, "height": 4}]')))
            self.assertEqual(sum_read, sum_expected)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            result = file.read()
            self.assertEqual(result, '[]')

        # including square objects
        t1 = Square(10, 7, 2, 8)
        t2 = Square(2, 4)
        Square.save_to_file([t1, t2])
        with open("Square.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x), '[{"y": 2, "x": 7, '
                                        '"id": 8, "size": 10}, '
                                        '{"y": 0, "x": 4, "id": 1, '
                                        '"size": 2}]')))
            self.assertEqual(sum_read, sum_expected)

        t1 = Square(10, 7)
        t2 = Square(2, 4)
        Square.save_to_file([t1, t2])
        with open("Square.json", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lamdba x: ord(x), '[{"y": 0, "x": 7, '
                                        '"id": 2, "size": 10}, '
                                        '{"y": 0, "x": 4, "id": 3, '
                                        '"size": 2}]')))
            self.assertEqual(sum_read, sum_expected)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_square(self):
        Square.save_file([])
        with open("Square.json", "r") as f:
            result = f.read()
            self.assertEqual(result, '[]')

    def test_from_json_string(self):
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                        {'height': 7, 'width': 1, 'id': 7}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                        {'height': 7, 'width': 1, 'id': 7,
                                         'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = [
                    {'id': 89, 'width': 10, 'height': 4, 'x': 3, 'y': 2},
                    {'id': 7, 'width': 1, 'height': 7, 'x': 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,[{'height': 4, 'width': 10, 'id': 89,
                                        'x': 3, 'y': 2},
                                        {'height': 7, 'width': 1,
                                        'id': 7, 'x': 3}])
        self.assertTrue(type(list_output) == list)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_imput)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

    def test_create(self):
        # checks create Rectangle
        t1 = Rectangle(3, 5, 1)
        t1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t1_dictionary)
        self.assertEqual(str(t2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(t1 is t2)
        self.assertFalse(t1 == t2)

        t1 = Rectangle(3, 5)
        t1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t2_dictionary)
        self.assertEqual(str(t2), "[Rectangle] (3) 0/0 - 3/5")
        self.assertFalse(t1 is t2)
        self.assertFalse(t1 == t2)

        t1 = Rectangle(3, 5, 3, 4, 89)
        t2_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t2_dictionary)
        self.assertEqual(str(t2), "[Rectangle] (89) 3/4 - 3/5")
        self.assertFalse(t1 is t2)
        self.assertFalse(t1 == t2)

        t1 = Rectangle(3, 5, 3, 4)
        t1_dictionary = t1.to_dictionary()
        t2 = Rectangle.create(**t1_dictionary)
        self.assertEqual(str(t2), "[Rectangle] (6) 3/4 - 3/5")
        self.assertFalse(t1 is t2)
        self.assertFalse(t1 == t2)

        # Checks for square creation
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (8) 5/1 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (10) 5/0 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5, 3, 89)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (89) 5/3 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(50)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (13) 0/0 - 50")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """ try loading from file """
        # check for rectangle load for file
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output), "[]")

        t1 = Rectangle(10, 7, 2, 8)
        t2 = Rectangle(2, 4)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))

        t1 = Rectangle(10, 50)
        t2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))

        t1 = Rectangle(10, 50)
        t2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))

        #Check for square load from file
        list_square_output = Square.load_from_file()
        self.assertEqual(str(list_square_output), "[]")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 0, 0, 89)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 4, 0, 0)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

    def test_save_csv(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file::
            self.assertEqual(file.read(), '[]')

        t1 = Rectangle(10, 7, 2, 8)
        t2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([t1, t2])
        sum_expected = sum(list(map(lambda x: ord(x), 'id,width,height,x,y\n'
                                    '1,10,7,2,8\n'
                                    '2,2,4,0,0\n')))
        with open("Rectangle.csv", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x),
                                        'id,width,height,x,y\n'
                                        '3,10,7,0,0\n'
                                        '4,2,4,0,0\n')))
            self.assertEqual(sum_read,sum_expected)

    def test_load_csv(self):

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output), "[]")

        t1 = Rectangle(10, 7, 2, 8)
        t2 = Rectangle(2, 4)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))


        t1 = Rectangle(10, 50)
        t2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))

        t1 = Rectangle(10, 50)
        t2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [t1, t2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(t1), str(list_rectangles_output[0]))
        self.assertEqual(str(t2), str(list_rectangles_output[1]))

    def reset(self):
        """ Resets class """
        Base.__Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
