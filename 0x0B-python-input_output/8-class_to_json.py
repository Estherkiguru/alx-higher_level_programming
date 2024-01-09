#!/usr/bin/python3
"""module for dictionary description"""


def class_to_json(obj):
    """returns the dictionary with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
