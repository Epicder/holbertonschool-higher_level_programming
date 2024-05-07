#!/usr/bin/python3
for c in (chr(i) for i in range(97, 123)):
    if c != chr(101) and c != chr(113):
        print (f"{c}", end="")
