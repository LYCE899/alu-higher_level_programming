#!/usr/bin/python3
'''Appending a string and returning the number of characters added'''


def append_write(filename="", text=""):
    '''Function that appends a string file'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
