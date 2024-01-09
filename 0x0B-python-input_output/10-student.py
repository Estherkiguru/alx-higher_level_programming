#!/usr/bin/python3
"""contains the class student with filters"""

class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns retrieves a dictionary representation of a Student
        If attrs is a list of strings, only attribute names contained 
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved"""
        
        try:
            if attrs is None:
                return self.__dict__
            else:
                return {attr: getattr(self, attr) for attr in attrs}
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key,value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
