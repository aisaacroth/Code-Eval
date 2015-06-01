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

        for (int i = 1; i < count + 1; ++i) {
            printf(" ");

            if (i % first_div == 0) {
                printf("F");
            }

            if (i % sec_div == 0) {
                printf("B");
            }

            if (i % first_div && i % sec_div) {
                printf("%d", i);
            }

        }

        printf("\n");
    }

    fclose(fp);
    return 0;
}
