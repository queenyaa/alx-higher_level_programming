#!/usr/bin/python3

for ascii_val in range(ord('Z'), ord('A') - 1, -1):
    if (ascii_val - ord('A')) % 2 == 0:
        char = chr(ascii_val)
    else:
        char = chr(ascii_val + ord('a') - ord('A'))
    print(char, end="")
print()
