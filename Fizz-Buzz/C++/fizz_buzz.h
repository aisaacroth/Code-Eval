#ifndef __FIZZ_BUZZ_H__
#define __FIZZ_BUZZ_H__

#include <cstdlib>
#include <fstream>
#include <iostream>

class FizzBuzz {
    private:
        const int first;
        const int second;
        const int count;
    public:
        FizzBuzz(int first, int second, int count);
        void evaluate();
};

#endif
