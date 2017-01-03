#!/usr/bin/env python3
"""
Self-describing number program.

Author: Alexander Roth
Date:   2017-01-02
"""

import argparse
from collections import Counter


def main():
    arguments = collect_arguments()
    testcases = retrieve_lines(arguments.file)

    for testcase in testcases:
        counter = check_self_describing(testcase)
        display_result(counter)


def collect_arguments():
    parser = argparse.ArgumentParser(description="Self-describing number"
                                     "program")
    parser.add_argument("file", type=str, help="path to file")
    return parser.parse_args()


def retrieve_lines(filename):
    with open(filename, 'r') as input_file:
        return [testcase.strip() for testcase in input_file]


def check_self_describing(testcase):
    describing_counter = Counter({k: int(v) for k, v in enumerate(testcase)})
    describing_counter.subtract(map(int, testcase))
    return not any(describing_counter.values())


def display_result(result):
    print("0" if not result else "1")


if __name__ == "__main__":
    main()
