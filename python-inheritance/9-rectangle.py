#!/usr/bin/python3
'''Creating class Rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creating a class that inherits properties from BaseGeometry'''

    def __init__(self, width, height):
        '''Function that takes in width and height'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''Defining an area function'''
        return self.__height * self.__width

    def __str__(self):
        '''Returns [Rectangle] '''
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
