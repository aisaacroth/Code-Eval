#!/usr/bin/env python3
"""
Fibonacci series up to the given integer.

Author: Alexander Roth
Date:   2017-01-24
"""

import argparse


def main():
    arguments = collect_arguments()

    for item in retrieve_lines(arguments.file):
        print(find_fibonacci(item))


def collect_arguments():
    parser = argparse.ArgumentParser(description="Fibonacci series program")
    parser.add_argument("file", type=str, help="path to test file")
    return parser.parse_args()


def retrieve_lines(filename):
    with open(filename, 'r') as input_file:
        for testcase in input_file:
            yield int(testcase.strip())


def find_fibonacci(value):
    fib = fibonacci()
    next(fib)

    for i in range(value - 1):
        next(fib)

    return next(fib)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    main()
