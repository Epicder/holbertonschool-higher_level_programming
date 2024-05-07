#!/usr/bin/python3
abcdary = "".join(chr(i) for i in range(97, 123) if chr(i) not in ['e', 'q'])
print("{}".format(abcdary), end="")
