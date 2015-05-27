#!/usr/bin/env python3.4
''' Tester for the Fizz Buzz program.

Author: Alexander Roth
Date:   2015-05-27
'''
from fizz_buzz import compose_answer_list, form_str_from_list
from fizz_buzz import read_test_cases, separate_variables
import unittest

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.test_list_1 = ['3 5 15']
        self.test_check_1 = ['1', '2', 'F', '4', 'B', 'F', '7', '8', 'F', 'B',
                '11', 'F', '13', '14', 'FB']
        self.test_check_2 = '1 2 F 4 B F 7 8 F B 11 F 13 14 FB'

    def test_read_test_cases(self):
        test_ans = read_test_cases(self.filename)
        self.assertIsNotNone(test_ans)
        self.assertEqual(test_ans[0], '3 5 15')

    def test_separate_variables(self):
        check = [3, 5, 15]
        for t1, t2, t3 in separate_variables(self.test_list_1):
            self.assertIsNotNone(t1)
            self.assertIsNotNone(t2)
            self.assertIsNotNone(t3)

            self.assertEqual(t1, check[0])
            self.assertEqual(t2, check[1])
            self.assertEqual(t3, check[2])

    def test_generate_answer_list(self):
        test_answer = compose_answer_list(3, 5, 15)
        self.assertEqual(test_answer, self.test_check_1)

    def test_form_str_from_list(self):
        test_string = form_str_from_list(self.test_check_1)
        self.assertEqual(test_string, self.test_check_2)


if __name__ == '__main__':
    unittest.main()
