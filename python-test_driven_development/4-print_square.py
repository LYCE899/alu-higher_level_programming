#!/usr/bin/python3
"""Printing a square with #"""


def print_square(size):
    """Function that prints a square where
    - size is the size legth of the square
    - size must be an integer else raises a TypeError exception with mssg
    - if size < 0, raise a ValueError with mssg
    - if size is a float & < 0, a TypeError exception with mssg is raised
    """
    square_c = "#"
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print(square_c, end="")
        print()
