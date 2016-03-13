#!/usr/bin/env python3

'''

Author: Alexander Roth
Date:   2016-03-13
'''
import sys


def main(args):
    in_file = args[1]
    line_generator = read_file(in_file)

    try:
        while True:
            line = next(line_generator)
            real_num = int(line)
            test_num = gen_armstrong_number(line)
            check_armstrong_number(real_num, test_num)
    except StopIteration:
        pass


def read_file(filename):
    assert type(filename) is str

    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()


def gen_armstrong_number(line):
    assert type(line) is str

    total = 0
    for i in line:
        total += int(i) ** len(line)
    return total


def check_armstrong_number(real_num, test_num):
    assert type(real_num) is int
    assert type(test_num) is int

    print('True') if real_num == test_num else print('False')


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
