#!/usr/bin/env python3

'''
Test suite for the cocktail sort program.

Author: Alexander Roth
Date:   2016-01-15
'''

import unittest

class TestCocktailSort(unittest.TestCase):

    def setUp(self):
        self.one_iter_list = [5, 4, 9, 10, 7, 3, 2, 1, 6]
        self.three_iter_list = [9, 8 , 7, 6, 5, 4, 3, 2, 1]


if __name__ == '__main__':
    unittest.main()
