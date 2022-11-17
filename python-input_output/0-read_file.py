#!/usr/bin/python3
'''Function that reads a text files and prints out its stdout'''


def read_file(filename=""):
    '''Defining a function that reads a text file'''
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
