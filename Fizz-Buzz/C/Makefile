CC      = gcc
CCFLAGS = -g -Wall -Werror
LDFLAGS = -g
EXES    = fizz_bizz fizz_test

.PHONY: default
default: $(EXES)

fizz_bizz: fizz_bizz.o
	$(CC) fizz_bizz.o $(LDFLAGS) -o fizz_bizz

fizz_bizz.o: fizz_bizz.c fizz_bizz.h
	$(CC) -c fizz_bizz.c $(CCFLAGS)

fizz_test: fizz_test.o
	$(CC) fizz_test.o $(LDFLAGS) -o fizz_test

fizz_test.o: fizz_test.c fizz_test.h fizz_bizz.h
	$(CC) fizz_test.c $(CCFLAGS)

.PHONY: clean
clean:
	rm -rf *~ a.out $(EXES)
