#!/usr/bin/python3
"""This module  reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads and prints filename with utf-8"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
