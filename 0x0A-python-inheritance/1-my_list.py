#!/usr/bin/python3
"""defines a class MyList that inherits from list"""


class MyList(list):
    """implements print sorting for the list class"""
    def print_sorted(self):
        """prints the list in an ascending order"""
        self.sort()
        print(self)
