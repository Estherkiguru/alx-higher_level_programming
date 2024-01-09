#!/usr/bin/python3
"""module that writes to a file"""


def write_file(filename="", text=""):
    """writes a string with utf-8 to return no. of characters"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
