#!/usr/bin/python3

def fizzbuzz():
    for numbers in range(1, 101):
        numcpy = numbers % 3
        numcpyy = numbers % 5
        if(numcpy == 0):
            print("Fizz", end=" ")
        elif(numcpyy == 0):
            print("Buzz", end=" ")
        else:
            print(f"{numbers}", end=" ")
    
