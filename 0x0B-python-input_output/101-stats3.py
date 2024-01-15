#!/usr/bin/python3

"""
Reads stdin line by line and computes
metrics
"""

def prt_stats(size, status_codes):
    """
    Prints metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == '__main__':
    import sys

    sz = 0
    status_codes = {}
    val_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for lyn in sys.stdin:
            if cnt == 10:
                prt_stats(sz, status_codes)
                cnt = 1
            else:
                cnt += 1

            lyn = lyn.split()

            try:
                sz += int(lyn[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lyn[-2] in val_codes:
                    if lyn[-2] not in status_codes:
                        status_codes[lyn[-2]] = 0
                    status_codes[lyn[-2]] += 1
            except IndexError:
                pass

        prt_stats(sz, status_codes)

    except KeyboardInterrupt:
        prt_stats(sz, status_codes)
        raise
