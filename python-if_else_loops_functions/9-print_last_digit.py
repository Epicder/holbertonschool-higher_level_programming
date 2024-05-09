#!/usr/bin/python3

def print_last_digit(number):
    if number == 0:
        print("{}".format(number), end="")
    elif number < 0:
        numcpy = abs(number)
        lastnum = numcpy % 10
        lastnum += 5
        lastnum += 1
        print("{}".format(lastnum), end="")
    elif number > 0:
        lastnum = number % 10
        print("{}".format(lastnum), end="")
    return number % 10
