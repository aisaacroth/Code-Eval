#!/usr/bin/env python3
'''
Module that has runs the sum of digit program.

Author: Alexander Roth
Date:   2016-01-15
'''

import sys


def main(args):
    in_filename = args[1]
    testcases = read_file(in_filename)
    for test in testcases:
        print(sum_digit(test))


def read_file(filename):
    with open(filename, 'r') as open_file:
        return [int(i.strip()) for i in open_file]


def sum_digit(number):
    if number < 10:
        return number
    return number % 10 + sum_digit(number // 10)


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
