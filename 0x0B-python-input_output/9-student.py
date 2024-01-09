#!/usr/bin/python3
"""module for class student"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """initializing the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of a student instances"""
        return self.__dict__
