# Makefile for the Bit Position program.
# 
# Author: Alexander Roth
# Date:   2015-11-25

CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
OBJS = bit-position.o test-bit-position.o
EXES = bit-position test-bit-position

.PHONY: tests
tests: $(EXES)

bit-position: bit-position.o
	$(CC) $(LDFLAGS) bit-position.o -o bit-position

bit-position.o: bit-position.c bit-position.c
	$(CC) -c $(CFLAGS) bit-position.c

test-bit-position: test-bit-position.o
	$(CC) $(LDFLAGS) test-bit-position.o -o test-bit-position

test-bit-position.o: test-bit-position.c bit-position.h
	$(CC) -c $(CFLAGS) test-bit-position.c

.PHONY: clean
clean:
	rm -f *.o *~ a.out $(OBS) $(EXES)

.PHONY: all
all: clean tests
