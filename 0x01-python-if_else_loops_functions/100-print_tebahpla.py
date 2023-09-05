#!/usr/bin/python3

upper = False
for ascii_val in range(-122, -96):
    ascii_val = -ascii_val
    if upper:
        ascii_val = ascii_val - (ord('a') - ord('A'))
    print("{character}".format(character=chr(ascii_val)), end="")
    upper = not upper
