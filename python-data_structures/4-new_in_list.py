#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        my_listcp = my_list.copy()
        return my_lsitcp
    else:
        my_listcp = my_list.copy()
        my_listcp[idx] = element
        return my_listcp
