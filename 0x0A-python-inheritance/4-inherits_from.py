#!/usr/bin/python3
"""module for only sub class of"""


def inherits_from(obj, a_class):
    """checks if an object is a true subclass"""
    return isinstance(obj, a_class) and type(obj) is not a_class
