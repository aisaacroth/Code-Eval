#!/usr/bin/env python3

'''
Test suite for the cocktail sort program.

Author: Alexander Roth
Date:   2016-01-15
'''

from cocktail_sort import cocktail_sort, read_file, split_line
import unittest


class TestCocktailSort(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.one_iter_line = '5 4 9 10 7 3 2 1 6 | 1'
        self.three_iter_line = '9 8 7 6 5 4 3 2 1 | 3'
        self.one_iter_list = [5, 4, 9, 10, 7, 3, 2, 1, 6]
        self.three_iter_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_read_file(self):
        test_ans = read_file(self.filename)
        exp_ans = '5 4 9 10 7 3 2 1 6 | 1'
        first_iter = next(test_ans)

        self.assertIsNotNone(first_iter)
        self.assertEqual(exp_ans, first_iter)

        exp_ans = '9 8 7 6 5 4 3 2 1 | 3'
        second_iter = next(test_ans)

        self.assertIsNotNone(second_iter)
        self.assertEqual(exp_ans, second_iter)

    def test_split_line(self):
        test_ans = split_line(self.one_iter_line)
        exp_ans = ([5, 4, 9, 10, 7, 3, 2, 1, 6], 1)

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans[0], test_ans[0])
        self.assertEqual(exp_ans[1], test_ans[1])
        self.assertEqual(exp_ans, test_ans)

        test_ans = split_line(self.three_iter_line)
        exp_ans = ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans[0], test_ans[0])
        self.assertEqual(exp_ans[1], test_ans[1])
        self.assertEqual(exp_ans, test_ans)

    def test_cocktail_sort(self):
        test_ans = cocktail_sort(self.one_iter_list, 1)
        exp_ans = [1, 4, 5, 9, 7, 3, 2, 6, 10]

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)

        test_ans = cocktail_sort(self.three_iter_list, 3)
        exp_ans = [1, 2, 3, 6, 5, 4, 7, 8, 9]

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)


if __name__ == '__main__':
    unittest.main()
