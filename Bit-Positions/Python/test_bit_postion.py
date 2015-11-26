#!/usr/bin/env python3
''' Tester for the Bit Position program.

Author: Alexander Roth
Date:   2015-11-25
'''
from bit_position import check_bits, dec_to_bin, match_check
import unittest

class TestBitPosition(unittest.TestCase):

    def setUp(self):
        pass

    def test_generate_dec_to_bin(self):
        test_ans = dec_to_bin(10)
        self.assertIsNotNone(test_ans)
        self.assertEqual(test_ans, [1, 0, 1, 0])

    def test_check_bits(self):
        ten = [1, 0, 1, 0]
        test_ans = check_bits(ten, 1, 2)
        self.assertFalse(test_ans)

        test_ans = check_bits(ten, 1, 3)
        self.assertTrue(test_ans)

        test_ans = check_bits(ten, 2, 4)
        self.assertTrue(test_ans)

    def test_match_check(self):
        check = 1
        test_ans = match_check(check)
        self.assertEqual(test_ans, "true")

        check = 0
        test_ans = match_check(check)
        self.assertEqual(test_ans, "false")

        check = 2
        test_ans = match_check(check)
        self.assertEqual(test_ans, "true")


if __name__ == '__main__':
    unittest.main()
