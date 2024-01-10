#!/usr/bin/python3
"""module for say my name"""


def say_my_name(first_name, last_name=""):
    """function that print the first and last name

    Args:
    first_name:string for the first name
    last_name:string for the last name

    Raises:
    TypeError:first_name or last_name must be a string
    """
    if not isinstance(first_name, str):
        return TypeError('first_name must be a string')
    if not isinstance(first_name, str):
        return TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
