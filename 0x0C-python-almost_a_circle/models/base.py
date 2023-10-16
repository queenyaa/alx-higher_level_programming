#!/usr/bin/python3

"""
Creating the "base" class which will serve as the foundatoin
for other classes
"""
import json
import csv
import os
import turtle


class Base:
    """
    Class to serve as the foundation
    for other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        # if id is provided, set it as a public instance attribute
        if id is not None:
            self.id = id
        else:
            """
            if id is not provided, increment __nb_objects and assign
            it to the id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of
        list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dictionaries)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented
        by the JSON
        """
        if json_string is None or len(json_string) == 0 or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create and return an instance with attributes set
        from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            # create a dummy rectangle instance
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            # Create a dummy square instance
            instance = cls(1)
        else:
            return None  # invalid class name

        # Update the instance with the dictionary value
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances based on the data
        stored in a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                data = file.read()
                if data:
                    list_dicts = cls.from_json_string(data)
                    return [cls.create(**d) for d in list_dicts]
                return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize and save instances to a CSV file """
        filename = cls.__name__ + ".csv"
        if cls == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        elif cls == "Square":
            fields = ["id", "size", "x", "y"]
        else:
            return
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            write.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize and load instances from a CSV file """
        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            return [
                    cls.create(**{k: int(v) for k, v in row.items()})
                    for row in reader
            ]

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(1)  # set the drawing speed

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.fillcolor("blue")  # Change the fill color
            t.begin_fill()
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.end_fill()

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.fillcolor("red")  # Change the fill color
            t.begin_fill()
            for _ in range(4):
                t.forward(square.size)
                t.let(90)
            t.end_fill()

        screen.exitonclick()
