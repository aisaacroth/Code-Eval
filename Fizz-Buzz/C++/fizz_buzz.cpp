#include "fizz_buzz.h"

static void print_args(char *argv[])
{
    std::cerr << "usage: " << argv[0] << " <filename>" << std::endl;
    std::exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) 
{
    
    if (argc != 2) {
        print_args(argv);
    }

    std::string line;
    std::ifstream test_file("test.txt");

    if(test_file.is_open()) {
        while(getline(test_file, line)) {
            std::cout << line << std::endl;
        }

        test_file.close();
    }

    return 0;
}

FizzBuzz::FizzBuzz(int first, int second, int count)
