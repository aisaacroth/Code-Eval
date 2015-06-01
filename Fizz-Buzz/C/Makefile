CC      = gcc
CCFLAGS = -g -std=c11 -Wall -Werror
LDFLAGS = -g
EXES    = fizz_buzz fizz_test

.PHONY: default
default: $(EXES)

fizz_buzz: fizz_buzz.o
	$(CC) fizz_buzz.o $(LDFLAGS) -o fizz_buzz

fizz_buzz.o: fizz_buzz.c fizz_buzz.h
	$(CC) -c fizz_buzz.c $(CCFLAGS)

fizz_test: fizz_test.o
	$(CC) fizz_test.o $(LDFLAGS) -o fizz_test

fizz_test.o: fizz_test.c fizz_test.h fizz_buzz.h
	$(CC) -c fizz_test.c $(CCFLAGS)

.PHONY: clean
clean:
	rm -rf *~ *.o a.out $(EXES)

.PHONY: all
all: clean default
