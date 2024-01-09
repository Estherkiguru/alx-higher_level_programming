#!/usr/bin/python3
"""module for creating an object from a JSON file"""


import json


def load_from_json_file(filename):
    """create object from a json file"""
    with open(filename, 'r') as file:
        json.load(file)
