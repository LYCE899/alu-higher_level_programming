#!/usr/bin/python3
'''Writing a class MyList that inherits from list'''


class MyList(list):
    '''Creating a superclass list'''

    def print_sorted(self):
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
