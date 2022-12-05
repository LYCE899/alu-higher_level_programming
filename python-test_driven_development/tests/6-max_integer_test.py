#!/usr/bin/python3
""""Using unittest"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class MaxInteger(unittest.TestCase):
    """"Creating a class"""

    def test_simple_case(self):
        """"Defining a function for a simple case"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """"Defining a function for a -ve case"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """"Defining a function for () case"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """"Defining a function for a middle case"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_case(self):
        """"Defining a function for a one element case"""
        self.assertEqual(max_integer([5]), 5)
