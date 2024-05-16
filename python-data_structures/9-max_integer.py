#!/usr/bin/python3

def max_integer(my_list=[]):
    for i in range (len(my_list)):
        if my_list[i] > my_list[i+1]:
            biggest = my_list[i]
            return biggest
