#!/usr/bin/python3
"""class Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.validate_integer("width", value, False)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The rectangle's x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value, False)
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The rectangle's y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value, False)
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validate the attributes of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
         if eq and value < 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be >= 0".format(name))
