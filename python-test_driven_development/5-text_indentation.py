#!/usr/bin/python3
"""Printing a text with two lines"""


def text_indentation(text):
    """Function that prints a text with 2 new line
    - text must be a string else a TypeError is raised"""
    if type(text) != str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)]
        )

    print("{}".format(text), end="")
