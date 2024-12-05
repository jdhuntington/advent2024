#!/usr/bin/env python3

import unittest

from problem1 import rotate_45
from problem1 import rotate_315

class TestRotate45(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(rotate_45([]), [])

    def test_single_element(self):
        self.assertEqual(rotate_45(['a']), ['a'])

    def test_two_characters(self):
        self.assertEqual(rotate_45(['ab']), ['a ', ' b'])

    def test_3x3(self):
        expected = ['a  ',
                    'db ',
                    'gec',
                    ' hf',
		    '  i']
        sample = ['abc','def','ghi']
        self.assertEqual(rotate_45(sample), expected)


class TestRotate315(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(rotate_315([]), [])

    def test_single_element(self):
        self.assertEqual(rotate_315(['a']), ['a'])

    def test_two_characters(self):
        self.assertEqual(rotate_315(['ab']), [' b', 'a '])

    def test_3x3(self):
        expected = ['  c',
                    ' bf',
                    'aei',
                    'dh ',
		    'g  ']
        sample = ['abc','def','ghi']
        self.assertEqual(rotate_315(sample), expected)

if __name__ == '__main__':
    unittest.main()
