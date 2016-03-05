#!/usr/bin/env python3

'''

Author: Alexander Roth
Date:   2016-03-05
'''
import sys


def main(args):
    in_file = args[1]
    line_generator = read_file(in_file)

    try:
        while True:
            line = next(line_generator)
            num_string = gen_num_string(line)
            total = sum_num_string(num_string)
            print_check(total)
    except StopIteration:
        pass


def read_file(filename):
    assert type(filename) is str

    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()


def gen_num_string(line):
    return ''.join(line.split())


def sum_num_string(line):
    num_list = [int(line[i]) if i % 2 else int(line[i]) * 2
                for i in range(len(line))]
    return sum(num_list)


def print_check(total):
    print('Fake') if total % 10 else print('Real')


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
