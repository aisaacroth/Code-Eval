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
            first_set, second_set = gen_sets(line)
            result = check_sets(first_set, second_set)
            print_result(result)
    except StopIteration:
        pass


def read_file(filename):
    assert type(filename) is str

    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()


def gen_sets(line):
    master = []
    set_list = []

    for item in line.split(','):
        if item.isdigit():
            set_list.append(int(item))
        else:
            end, begin = item.split(';')
            set_list.append(int(end))
            master.append(set(set_list))
            set_list = [int(begin)]

    master.append(set(set_list))
    return master


def check_sets(first_set, second_set):
    return first_set & second_set


def print_result(result):
    int_set = list(result) if result else None
    print(','.join([str(i) for i in int_set])) if int_set else print()


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
