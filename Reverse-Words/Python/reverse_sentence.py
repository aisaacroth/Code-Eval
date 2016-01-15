#!/usr/bin/env python3
'''
Module that reverses a sentence.

Author: Alexander Roth
Date:   2016-01-15
'''

import sys

def main(args):
    in_filename = args[1]

    with open(in_filename, 'r') as in_file:
        for line in in_file:
            print(reverse_sentence(line))


def reverse_sentence(line):
    return ' '.join(reversed(line.split()))


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
