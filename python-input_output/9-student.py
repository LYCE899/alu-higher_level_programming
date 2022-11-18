#!/usr/bin/python3
'''Writing class student'''


class Student:
    '''Defining a class called student'''
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        '''Instantiation of data given'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieving a dictionary representation'''
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return context
