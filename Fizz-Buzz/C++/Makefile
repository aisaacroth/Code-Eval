# Makefile for the FizzBuzz C++ program.
#
# Author: Alexander Roth
# Date:   2015-07-09

CXX     = g++-5
CXXFLAGS = -g -std=c++14 -Wall -Werror
LDFLAGS = -g
EXES    = fizz_buzz

.PHONY: default
default: $(EXES)
	
fizz_buzz: fizz_buzz.o
	$(CXX) fizz_buzz.o $(LDFLAGS) -o fizz_buzz

fizz_buzz.o: fizz_buzz.h fizz_buzz.cpp
	$(CXX) -c fizz_buzz.cpp $(CXXFLAGS)

.PHONY: clean
clean:
	rm -rf *~ *.o a.out fizz_buzz.dSYM $(EXES)

.PHONY: all
all: clean default
