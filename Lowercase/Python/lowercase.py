#!/usr/bin/env python3.4
'''

Author: Alexander Roth
Date:   2015-07-03
'''
import sys

def print_arguments(program_name):
    print("python3.4 {} <filename>".format(program_name))


def main(filename):
    with open(filename, 'r') as src_file:
        for line in src_file:
            if line.islower():
                print(line.rstrip())
            else:
                print(line.lower().rstrip())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_arguments(sys.argv[0])
    else:
        main(sys.argv[1])
