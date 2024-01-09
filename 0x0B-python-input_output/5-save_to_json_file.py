#!/usr/python3
"""Saving an object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Write using JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
