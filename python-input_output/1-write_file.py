#!/usr/bin/python3
'''Function that writes a string and returns the number of characters'''


def write_file(filename="", text=""):
    '''Defining a function that writes a string
    returning the number of characters'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
