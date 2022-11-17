#!/usr/bin/python3
'''A function that tells if an object is an instance of specified class'''


def is_same_class(obj, a_class):
    '''Function that verifies if an object is exactly an instance of a class'''
    return type(obj) is a_class
