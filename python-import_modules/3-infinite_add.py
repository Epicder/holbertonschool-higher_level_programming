#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1) == 0:
        print("0")
    else:
        sum = 0
        for i in range(1, (len(sys.argv))):
            sum += int(sys.argv[i])

        print(sum)
