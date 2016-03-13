#!/usr/bin/env python3
'''
Test suite for the Armstrong number program.

Author: Alexander Roth
Date:   2016-03-13
'''

from find_armstrong import gen_armstrong_number, check_armstrong_number
from find_armstrong import read_file
import unittest


class TestArmstrongNumber(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.test_6 = '6'
        self.test_153 = '153'
        self.test_351 = '351'

    def test_read_file(self):
        test_iter = read_file(self.filename)
        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('6', test_ans)

        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('153', test_ans)

        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('351', test_ans)

    def test_gen_armstrong_number(self):
        test_ans = gen_armstrong_number(self.test_6)

        self.assertIsNotNone(test_ans)
        self.assertEqual(6, test_ans)

        test_ans = gen_armstrong_number(self.test_153)

        self.assertIsNotNone(test_ans)
        self.assertEqual(153, test_ans)

        test_ans = gen_armstrong_number(self.test_351)

        self.assertIsNotNone(test_ans)
        self.assertEqual(153, test_ans)


if __name__ == '__main__':
    unittest.main()
