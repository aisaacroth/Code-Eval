#!/usr/bin/env python3.4
'''

Author: Alexander Roth
Date:   2015-05-27
'''
import sys

def print_arguments(program_name):
    print("python3.4 {} <filename>".format(program_name))


def main(filename):
    test_cases = read_test_cases(filename)

    for x, y, n in separate_variables(test_cases):
        answer_list = compose_answer_list(x, y, n)
        answer_str = form_str_from_list(answer_list)
        print(answer_str)


def read_test_cases(filename):
    tests = []

    with open(filename, 'r') as src_file:
        tmp = src_file.readlines()
        tests = clean_lines(tmp)

    return tests


def clean_lines(line_list):
    clean_list = []

    for line in line_list:
        clean_list.append(line.strip())

    return clean_list


def separate_variables(line_list):
    for line in line_list:
        items = line.split()
        yield int(items[0]), int(items[1]), int(items[2])


def compose_answer_list(x, y, n):
    answer_list = []

    for i in range(1, n + 1) :
        ans = ''

        if i % x == 0:
            ans += 'F'

        if i % y == 0:
            ans += 'B'

        answer_list.append(ans or str(i))

    return answer_list


def form_str_from_list(answer_list):
    return ' '.join(answer_list)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_arguments(sys.argv[0])
    else:
        main(sys.argv[1])
