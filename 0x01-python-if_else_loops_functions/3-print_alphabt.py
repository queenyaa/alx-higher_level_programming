#!/usr/bin/python3

for ascii_val in range(ord('a'), ord('z') + 1):
    if ascii_val != ord('q') and ascii_val != ord('e'):
        print("{}".format(chr(ascii_val)), end="")
