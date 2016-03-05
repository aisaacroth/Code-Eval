#!/usr/bin/env python3

'''

Author: Alexander Roth
Date:   2016-03-05
'''

import sys


def main(args):
    in_file = args[1]
    line_generator = yield_line(in_file)

    try:
        while True:
            line = next(line_generator)
            num_list = split_line(line)
            uniq_list = gen_unique_list(num_list)
            print(','.join([str(i) for i in uniq_list]))
    except StopIteration:
        pass


def yield_line(filename):
    with open(filename, 'r') as open_file:
        for line in open_file:
            yield line.strip()


def split_line(line):
    assert type(line) is str

    split_line = line.split(',')
    return [int(item) for item in split_line]


def gen_unique_list(num_list):
    return list(set(num_list))


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
