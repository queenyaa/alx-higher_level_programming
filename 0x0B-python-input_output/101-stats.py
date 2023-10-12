#!/usr/bin/python3

"""
Program to read IP logs from stdin and print
metrics every 10 lines
"""


def print_sorted(stat_cd):
    """
    Print status codes with nonzero value
    """

    sort_key = sorted(stat_cd.keys())
    print('\n'.join(["{:d}: {:d}".format(g, stat_cd[g])
                        for g in sort_key if stat_cd[g] != 0]))


if __name__ == '__main__':
    import sys

    tot = 0
    stat_cd = \
            {cd: 0 for cd in [200, 300, 400, 401, 403, 404, 405, 500]}
    try:
        o = 0
        for lyn in sys.stdin:
            wds = lyn.split()
            try:
                file_size = int(wds[-1])
                tot += file_size
            except (IndexError, ValueError):
                pass

            try:
                code = int(wds[-2])
                if code in stat_cd:
                    stat_cd[code] += 1
            except (IndexError, ValueError):
                pass

            o += 1

            if o % 10 == 0:
                print("File size: {}".format(tot))
                print_sorted(stat_cd)

    except KeyboadInterrupt:
        print("File size: {}".format(tot))
        print_sorted(stat_cd)
