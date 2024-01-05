#!/usr/bin/python3
"""
Defines a class rectangle with width and height
"""


class Rectangle:
    """rectangle Representation"""
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
