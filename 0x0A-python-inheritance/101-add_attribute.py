#!/usr/bin/python3
"""module for adding attributes to objects"""


def add_attribute(obj, attr, value):
    """adds new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
