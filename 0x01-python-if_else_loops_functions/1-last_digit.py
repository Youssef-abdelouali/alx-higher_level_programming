#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
lastdig = int(number_str[-1])
if lastdig > 5:
    print(f"Last digit of {number} is {lastdig} and is greater than 5")
elif lastdig == 0:
    print(f"Last digit of {number} is {lastdig} and is 0")
else:
    print(f"Last digit of {number} is {lastdig} and is less than 6 and not 0")
