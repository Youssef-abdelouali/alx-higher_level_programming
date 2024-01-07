#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"The number {number} is positive")
elif number < 0:
    print("The number {} is negative ".format(number))
else:
    print(f"The number {number} is zero ")
