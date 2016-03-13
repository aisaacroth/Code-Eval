#!/usr/bin/env python3
'''
Testsuite for Set Intersection program.

Author: Alexander Roth
Date:   2016-03-13
'''

from set_intersection import gen_sets, read_file
import unittest


class TestSetIntersection(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.test_first_line = '1,2,3,4;4,5,6'
        self.test_second_line = '20,21,22;45,46,47'
        self.test_third_line = '7,8,9;8,9,10,11,12'

    def test_read_file(self):
        test_iter = read_file(self.filename)
        exp_ans = '1,2,3,4;4,5,6'
        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)

        exp_ans = '20,21,22;45,46,47'
        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)

        exp_ans = '7,8,9;8,9,10,11,12'
        test_ans = next(test_iter)

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)

    def test_gen_sets(self):
        test_ans = gen_sets(self.test_first_line)
        exp_ans = [{1,2,3,4},{4,5,6}]

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)

        test_ans = gen_sets(self.test_second_line)
        exp_ans = [{20,21,22},{45,46,47}]

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)
        
        test_ans = gen_sets(self.test_third_line)
        exp_ans = [{7,8,9},{8,9,10,11,12}]

        self.assertIsNotNone(test_ans)
        self.assertEqual(exp_ans, test_ans)
       

if __name__ == '__main__':
    unittest.main()

