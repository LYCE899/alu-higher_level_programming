#!/usr/bin/python3
'''Class square which inherits from Rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Creating a class square that inherits from Rectangle'''

    def __init__(self, size):
        '''Defining the init function'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Defining the area function'''
        return self.__size ** 2

    def __str__(self):
        '''Returns [Square]'''
        return str("[Square] {}/{}".format(self.__size, self.__size))
