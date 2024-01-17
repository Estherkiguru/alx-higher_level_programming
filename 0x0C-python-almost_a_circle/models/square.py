#!/usr/bin/python3
"""module for the class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
