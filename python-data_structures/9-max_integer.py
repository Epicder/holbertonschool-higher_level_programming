#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = my_list[0]
    for i in my_list:
        if i > biggest:
            biggest = i
        return biggest
