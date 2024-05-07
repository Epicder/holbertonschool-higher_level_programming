#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 == 0:
    last = number % 10
    print(f"Last digit of {number} is {last} and is 0")
elif number > 0 and number % 10 > 5:
    last = number % 10
    print(f"Last digit of {number} is {last} and is greater than 5")
elif number > 0 and number % 10 < 6:
    last = number % 10
    print(f"Last digit of {number} is {last} and is less than 6")
elif number < 0:
    abs_n = abs(number)
    last = abs_n % 10
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
