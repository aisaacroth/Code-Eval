#!/usr/bin/env python3
'''
Module that contains the cocktail sort algorithm.

Author: Alexander Roth
Date:   2016-01-15
'''

import sys

def main(args):
    in_file = args[1]
    line_generator = read_file(in_file)

    try:
        while True:
            line = next(line_generator)
            num_list, iterations = split_line(line)
            print(cocktail_sort(num_list, iterations))
    except StopIteration:
        pass


def read_file(filename):
    assert type(filename) is str

    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()


def split_line(line):
    assert type(line) is str

    split_list = line.split('|')
    iterations = int(split_list[1])

    nums = [int(i.strip()) for i in split_list[0].split()]
    return (nums, iterations)


def cocktail_sort(num_list, iterations):
    i = 0
    stop_right = len(num_list) - 1
    stop_left = -1

    while i < iterations:

        stop_left += 1
        for j in range(stop_left, stop_right):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

        stop_right -= 1
        for j in range(stop_right, stop_left - 1, -1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        
        i+= 1

    return num_list


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
