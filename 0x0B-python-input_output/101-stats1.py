#!/usr/bin/python3

"""
A Python script that reads line from standard input, processes and computer
the statistics as required
"""


if __name__ == '__main__':
    from sys import stdin

    cd_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    tot_size = 0

    try:
        x = 0
        for lyn in stdin:
            try:
                stripd = lyn.split()
                f_size = int(stripd[-1])
                tot_size += f_size
            except (IndexError, ValueError):
                pass

            try:
                cd = int(stripd[-2])
                if cd in cd_dict:
                    cd_dict[cd] += 1
            except (IndexError, ValueError):
                pass

            x += 1

            if x % 10 == 0:
                print("File size: {}".format(tot_size))
                for stat_cd in sorted(cd_dict.keys()):
                    if cd_dict[stat_cd] > 0:
                        print("{}: {}:".format(stat_cd, cd_dict[stat_cd]))

    except KeyboardInterrupt:
        print("File size: {}".format(tot_size))
        for stat_cd in sorted(cd_dict.keys()):
            if cd_dict[stat_cd] > 0:
                print("{}: {}".format(stat_cd, cd_dict[stat_cd]))
