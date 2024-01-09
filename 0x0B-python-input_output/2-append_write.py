#!/usr/bin/python3
"""module for appending to a file"""


def append_write(filename="", text=""):
    """Appends at end of a text file with utf-8"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
