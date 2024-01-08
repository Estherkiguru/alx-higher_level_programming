#!/usr/bin/python3
"""
Defines a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initializes a new Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
