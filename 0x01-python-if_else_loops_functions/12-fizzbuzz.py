#!/usr/bin/python3

def fizzbuzz():
    e = 1
    while e <= 100:
        if e % 3 == 0 and e % 5 == 0:
            print("FizzBuzz", end="")
        elif e % 3 == 0:
            print("Fizz", end="")
        elif e % 5 == 0:
            print("Buzz", end="")
        else:
            print(e, end="")

        if e != 100:
            print(" ", end="")
        e += 1
    print(" ", end="")
