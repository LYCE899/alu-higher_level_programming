#!/usr/bin/python3
'''Writing a function that checks if an object is
an instance of a class that is inherited directly or indirectly'''


def inherits_from(obj, a_class):
    '''Direct and indirect inheritance'''
    return isinstance(obj, a_class) and type(obj) != a_class
