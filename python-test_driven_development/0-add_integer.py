#!/usr/bin/python3
"""Adding two integers"""


def add_integer(a, b=98):
    """Function that adds two integers a and b
    Both integers must be integers or floats
    else raises a TypeError exception
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
