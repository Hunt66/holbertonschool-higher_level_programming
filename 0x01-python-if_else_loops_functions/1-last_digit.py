#!/usr/bin/python3

# this program makes a random number and prints the last diget of (that
# number) is (last digit) is greater than 5 less than 6 and not 0 or
# is zero

import random
number = random.randint(-10000, 10000)
if abs(number) % 10 > 5:
    if number >= 0:
        print("Last digit of {:d} is {:d} and is greater than 5"
              .format(number, abs(number) % 10))
    else:
        print("Last digit of {:d} is -{:d} and is greater than 5"
              .format(number, abs(number) % 10))
elif abs(number) % 10 < 6 and abs(number) % 10 != 0:
    if number >= 0:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0"
              .format(number, number % 10))
    else:
        print("Last digit of {:d} is -{:d} and is less than 6 and not 0"
              .format(number, abs(number) % 10))
else:
    if number >= 0:
        print("Last digit of {:d} is {:d} and is 0"
              .format(number, abs(number) % 10))
