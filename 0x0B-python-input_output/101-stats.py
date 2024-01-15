#!/usr/bin/python3

"""
Reads stdin line by line and computes
metrics
"""
import sys


file_size = 0
status_tal = {"200": 0, "300": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
x = 0
try:
    for line in sys.stdin:
        tok = line.split()
        if len(tok) >= 2:
            b = x
            if tok[-2] in status_tal:
                status_tal[tok[-2]] += 1
                x += 1
            try:
                file_size += int(tok[-1])
                if b == x:
                    x += 1
            except FileNotFoundError:
                if b == x:
                    continue
        if x % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tal.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tal.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tal.items()):
        if value:
            print("{:s}: {:d}".format(key,value))
