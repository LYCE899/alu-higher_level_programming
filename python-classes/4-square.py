#!/usr/bin/python3
'''Creating a class'''


class Square:
    '''Square class with an attribute'''
    def __init__(self, size=0):
        '''Instance attribute'''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns the area of a square'''
        return self.__size * self.__size
