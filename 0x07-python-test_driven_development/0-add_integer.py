#!/usr/bin/python3
"""module that adds two numbers"""


def add_integer(a, b=98):
    """adds two integers

    parameters:
    - a (int):First integer
    - b (int):second integer,set at a default of 98

    raises:
    TypeError if a, b are not float, int

    Returns
    int: The sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.file("tests/0-add_integer.txt")
