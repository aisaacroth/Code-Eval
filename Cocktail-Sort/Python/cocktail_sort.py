#!/usr/bin/env python3
'''
Module that contains the cocktail sort algorithm.

Author: Alexander Roth
Date:   2016-01-15
'''

import sys

def main(args):
    pass


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
