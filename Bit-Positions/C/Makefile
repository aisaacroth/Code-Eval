# Makefile for the Bit Position program.
# 
# Author: Alexander Roth
# Date:   2015-11-25

CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g

bit-position: bit-position.o
	$(CC) $(LDFLAGS) bit-position.o -o bit-position

bit-position.o: bit-position.c bit-position.c
	$(CC) -c $(CFLAGS) bit-position.c

.PHONY: clean
clean:
	rm -f *.o *~ a.out bit-position 

.PHONY: all
all: clean bit-position
