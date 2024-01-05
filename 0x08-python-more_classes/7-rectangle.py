#!/usr/bin/python3

"""
Defines a class rectangle with width and height
"""


class Rectangle:
    """rectangle Representation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if not self.__width or not self.__height:
            return ""
        return (
                (str(Rectangle.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """Returns a representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints the message Bye rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
