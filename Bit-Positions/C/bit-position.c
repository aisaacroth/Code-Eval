#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bit-position.h"

/*
 * Given a number and two integers, determine if the bits in the positions are
 * the same or not. Positions are 1-based.
 *
 * Author: Alexander Roth
 * Date:   2015-11-25
 */
static void printUsage();

int main(int argc, char **argv) {
    if (argc != 4) {
        printUsage();
    }
    
    int number = atoi(argv[1]);
    int pos_1 = atoi(argv[2]);
    int pos_2 = atoi(argv[3]);
    char *pointer = dec_to_bin(number);

    int check = check_bits(pointer, pos_1, pos_2);
    print_match(check);

    free(pointer);
    return 0;
}

static void printUsage() {
    fprintf(stderr, "usage: bit-position <number> <bit 1> <bit 2>\n");
    exit(1);
}

char *dec_to_bin(int num) {
    /* Converts the specified integer 'num' into its binary representation. */
    int count = 0;
    char *pointer = (char *)malloc(32 + 1);

    if (pointer == NULL) {
        exit(1);
    }

    int d;
    for (int c = 31; c >= 0; c--) {
        d = num >> c;

        if (d & 1) {
            *(pointer + count) = 1 + '0';
        } else {
            *(pointer + count) = 0 + '0';
        }

        count++;
    }

    *(pointer + count) = '\0';

    return pointer;
}

int check_bits(char *num, int pos_1, int pos_2) {
    /* Checks that the bits at the specified position are the same. */
    size_t len = strlen(num);
    if (num[len - pos_1] == num[len - pos_2]) {
        return 1;
    }
    return 0;
}

void print_match(int check) {
    /* Prints if the check value is non-negative */
    printf("%s", check ? "true": "false");
}
