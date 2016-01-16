#!/usr/bin/env python3
'''
Test suite for the sum digits program.

Author: Alexander Roth
Date:   2016-01-15
'''

from sum_digits import read_file, sum_digit
import unittest


class TestSumDigit(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.test_one = 23
        self.test_two = 496

    def test_read_file(self):
        test_ans = read_file(self.filename)

        self.assertIsNotNone(test_ans)
        self.assertEqual(self.test_one, test_ans[0])
        self.assertEqual(self.test_two, test_ans[1])
        self.assertEqual(2, len(test_ans))

    def test_sum_digit(self):
        test_ans = sum_digit(self.test_one)

        self.assertIsNotNone(test_ans)
        self.assertEqual(5, test_ans)

        test_ans = sum_digit(self.test_two)

        self.assertIsNotNone(test_ans)
        self.assertEqual(19, test_ans)


if __name__ == '__main__':
    unittest.main()
