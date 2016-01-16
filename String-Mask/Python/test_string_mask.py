#!/usr/bin/env python3
'''
Test suite for the String mask program.

Author: Alexander Roth
Date:   2016-01-15
'''

from string_mask import encode_string, read_file
import unittest


class TestStringMask(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.test_hello = ['hello', '11001']
        self.test_world = ['world', '10000']
        self.test_cba = ['cba', '111']

    def test_read_file(self):
        test_iter = read_file(self.filename)
        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('hello 11001', test_ans)

        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('world 10000', test_ans)

        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual('cba 111', test_ans)

    def test_encode_string(self):
        string = self.test_hello[0]
        encode = self.test_hello[1]
        test_ans = encode_string(string, encode)

        self.assertIsNotNone(test_ans)
        self.assertEqual('HEllO', test_ans)

        string = self.test_world[0]
        encode = self.test_world[1]
        test_ans = encode_string(string, encode)

        self.assertIsNotNone(test_ans)
        self.assertEqual('World', test_ans)

        string = self.test_cba[0]
        encode = self.test_cba[1]
        test_ans = encode_string(string, encode)

        self.assertIsNotNone(test_ans)
        self.assertEqual('CBA', test_ans)


if __name__ == '__main__':
    unittest.main()
