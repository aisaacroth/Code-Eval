Real-Fake
======

##Description##
The police caught a swindler with a big pile of credit cards. Some of them are stolen and some are fake. It would take too much time to determine which ones are real and which are fake, so you need to write a program to check credit cards.

To determine which credit cards are real, double every third number starting from the first one, add them together, and then add them to those figures that were not doubled. If the total sum of all numbers is divisible by 10 without remainder, then this credit card is real.

###Input Sample:###
The first argument is a path to a file. each row includes a test case with a credit card number that you will need to check.
```
9999 9999 9999 9999
9999 9999 9999 9993
```

###Output Sample:###
If a credit card is fake - print Fake, if it's real - Print Real.
```
Fake
Real
```

###Constraints:###
1. The credit card number is 16 digits in length.
2. The number of test cases is 40.