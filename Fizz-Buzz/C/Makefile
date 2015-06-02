CC      = gcc-5
CCFLAGS = -g -std=c11 -Wall -Werror
LDFLAGS = -g
EXES    = fizz_buzz

.PHONY: default
default: $(EXES)

fizz_buzz: fizz_buzz.o
	$(CC) fizz_buzz.o $(LDFLAGS) -o fizz_buzz

fizz_buzz.o: fizz_buzz.h fizz_buzz.c
	$(CC) -c fizz_buzz.c $(CCFLAGS)

.PHONY: clean
clean:
	rm -rf *~ *.o a.out fizz_buzz.dSYM $(EXES)

.PHONY: all
all: clean default
