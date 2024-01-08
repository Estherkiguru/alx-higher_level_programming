#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Represent a rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """override new to return an instance of MyInt"""
        return int.__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Override equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator"""
        return super().__eq__(other)
