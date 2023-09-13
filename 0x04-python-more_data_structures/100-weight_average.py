#!/usr/bin/python3


def weight_average(my_list=[]):

    if not my_list:
        return (0)

    tot_sc = 0
    tot_wght = 0

    for sc, wght in my_list:
        tot_sc += sc * wght
        tot_wght += wght

    if tot_wght == 0:
        return (0)

    return (tot_sc / tot_wght)
