#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            element = my_list[i]
            print("{:d}".format(element), end="")
            count += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            pass
        i += 1
    print()
    return count
            
