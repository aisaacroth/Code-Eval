#!/usr/bin/env python3
'''

Author: Alexander Roth
Date:   2015-11-25
'''
import sys


def main(args):
    num = int(args[1])
    pos_1 = int(args[2])
    pos_2 = int(args[3])

    binary = dec_to_bin(num)
    check = check_bits(binary, pos_1, pos_2)
    print(match_check(check))


def dec_to_bin(num):
    binary = []
    
    rem = num % 2
    value = num
    while value > 0:
        binary.append(rem)
        value = value // 2
        rem = value % 2

    return binary[::-1]


def check_bits(num, pos_1, pos_2):
    bin_lin = len(num)
    return num[bin_lin - pos_1] == num[bin_lin - pos_2]


def match_check(check):

    return "true" if check else "false"


def print_arguments():
    print("python3 {0} <num> <bit 1> <bit 2>".format(sys.argv[0]))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)
    else:
        print_arguments()

