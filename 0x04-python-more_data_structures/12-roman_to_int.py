#!/usr/bin/python3


def roman_to_int(roman_string):

    rom_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
            }

    if roman_string and isinstance(roman_string, str):
        tot = 0
        l_key = 0
        cur_key = 0

        for sym in roman_string:
            cur_key = rom_dict.get(sym, 0)
            if l_key != 0 and l_key >= cur_key:
                tot += cur_key
            elif l_key != 0 and l_key < cur_key:
                tot += (cur_key - (2 * l_key))
            elif l_key == 0:
                tot += cur_key
            l_key = cur_key
        return (tot)
    else:
        return (0)
