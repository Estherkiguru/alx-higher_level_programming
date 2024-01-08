#!/usr/bin/python3
"""module for a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """Calulates area of a square"""
        return self._size ** 2
