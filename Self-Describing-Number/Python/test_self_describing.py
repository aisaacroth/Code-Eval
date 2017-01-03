#!/usr/bin/env python3
"""
Test suite for the self-describing number program.

Author: Alexander Roth
Date:   2017-01-02
"""

from self_describing import check_self_describing
import unittest


class TestSelfDescribingNumber(unittest.TestCase):

    def test_good_number(self):
        test_result = check_self_describing("2020")
        self.assertTrue(test_result)

    def test_bad_number(self):
        test_result = check_self_describing("22")
        self.assertFalse(test_result)

    def test_large_good_number(self):
        test_result = check_self_describing("9210000001000")
        self.assertTrue(test_result)

    def test_zero(self):
        test_result = check_self_describing("0")
        self.assertFalse(test_result)

    def test_large_bad_number(self):
        test_result = check_self_describing("111111111111")
        self.assertFalse(test_result)


if __name__ == '__main__':
    unittest.main()
