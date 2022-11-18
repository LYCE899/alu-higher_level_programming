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

    def to_json(self, attrs=None):
        '''Returning a dictionary representation'''
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None or type(attrs) != list:
            return context
        else:
            cont = {}
            for item in attrs:
                if type(item) != str:
                    return context
                if item in context.keys():
                    cont[item] = context[item]
            return cont

    def reload_from_json(self, json):
        '''Reload_from_json'''
        for item in json.keys():
            self.__dict__[item] = json[item]
