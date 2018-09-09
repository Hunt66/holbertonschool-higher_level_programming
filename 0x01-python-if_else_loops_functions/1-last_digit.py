#!/usr/bin/python3

# this program makes a random number and prints the last diget of (that
# number) is (last digit) is greater than 5 less than 6 and not 0 or
# is zero

import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5" .format(
        number, number % 10))
elif number % 10 < 6:
    print("Last digit of {:d} is {:d} and is less than 6" .format(
              number, number % 10))
else:
    print("Last digit of {:d} is {:d} and is zero" .format(number,
                                                           number % 10))
