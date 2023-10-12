#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

filename = "file_not"
text_search = "c"
text_append = "Python"
try:
    append_after(filename, text_search, text_append)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
