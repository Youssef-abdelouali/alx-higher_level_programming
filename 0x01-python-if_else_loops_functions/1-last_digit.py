#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    _lasdig_ = number % -10
else:
    _lasdig_ = number % 10
if _lasdig_ > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, _lasdig_))
elif _lasdig_ < 6 and _lasdig_ != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, _lasdig_))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
