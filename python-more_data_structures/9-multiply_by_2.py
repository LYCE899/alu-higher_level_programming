#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(a_dictionary)
    for key, value in new_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
