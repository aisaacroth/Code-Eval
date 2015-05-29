#include "fizz_buzz.h"

static void die(const char *message)
{
    perror(message);
    exit(1);
}

static void print_args(char *argv[])
{
    fprintf(stderr, "usage: %s <filename>\n", argv[0]);
    exit(1);
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        print_args(argv);
    }

    char *filename = argv[1];
    FILE *fp = fopen(filename, "rb");

    if (fp == NULL) {
        die(filename);
    }

    char line[1024];

    while(fgets(line, sizeof(line), fp) != NULL) {

        char *end;

        long first_div = strtol(line, &end, 10);
        long sec_div = strtol(end, &end, 10);
        long count = strtol(end, &end, 10);
        printf("Divisor 1: %ld, Divisor 2: %ld, Count: %ld\n", first_div,
                sec_div, count);

        // Test the divisibility here.
        for (int i = 1; i < count + 1; ++i) {
            char *ans = NULL;

            if (i % first_div) {
                // Probably doing something with strcat here
            }

            if (i % sec_div) {
                // Again, use strcat
            }

            if (ans == NULL) {
                sprintf(ans, "%d", i);
            }

        }

    }

    fclose(fp);

    return 0;
}
