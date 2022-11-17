#!/usr/bin/python3
'''Creating class BaseGeometry'''


class BaseGeometry:
    '''Writing class BaseGeometry'''

    def area(self):
        '''Function that raises an exception with a message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Creating a function that validates the value'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
