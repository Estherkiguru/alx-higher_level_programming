#!/usr/bin/python3
"""Class Base module"""
import json
import csv


class Base:
    """Representation of the base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes object to CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                for obj in list_objs:
                    list_objs = [obj.id, obj.width, obj.height, obj.x, obj.y]
            else:
                for obj in list_objs:
                    list_objs = [obj.id, obj.size, obj.x, obj.y]
        with open("{}.csv".format(cls.__name__), 'w', newline='', encoging="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes list_obj from csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        loaded_objs = []
        with open("{}.csv".format(cls.__name__), 'r', newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = ("id": row[0], "width": row[1], "height":
                        row[2], "x": row[3], "y": row[4])
                else:
                d = ("id": row[0], "size": row[1], "x": row[2], "y": row[3])
                loaded_objs(cls.create(**d))
                return loaded_objs
