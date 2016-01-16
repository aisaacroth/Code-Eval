#!/usr/bin/env python3
'''
Module for the String Mask problem. Takes in a string and a binary encoding
that converts the string to either uppercase or lowercase per letter.

Author: Alexander Roth
Date:   2016-01-15
'''

import sys


def main(args):
    in_filename = args[1]
    line = read_file(in_filename)
    try:
        while True:
            string, encode = next(line).split()
            result = encode_string(string, encode)
            print(result)
    except StopIteration:
        pass


def read_file(filename):
    with open(filename, 'r') as open_file:
        for line in open_file:
            yield line.strip()


def encode_string(string, encode):
    return ''.join([string[i].upper() if encode[i] == '1' else string[i]
                    for i in range(len(string))])


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
