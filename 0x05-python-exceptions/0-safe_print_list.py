#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    cnt = 0 #initialize a counter to keep track of elements printed

    try:
        for d in range(x):
            print(my_list[d], end="")   #print without new line
            cnt += 1
    except IndexError:
        pass    #handle case where index is out of range

    print() #print newline char to separate the output
    return (cnt)
