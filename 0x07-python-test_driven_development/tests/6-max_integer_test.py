#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([1, 5, -5]), 5)
        self.assertAlmostEqual(max_integer([1, 5, -6]), 5)
        self.assertAlmostEqual(max_integer([1, 6, 8, 3]), 8)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer("abcdefghiaaaaa"), 'i')
        self.assertAlmostEqual(max_integer(['a', 'b', 'z']), 'z')
