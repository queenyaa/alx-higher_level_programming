#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    res = []
    for d in range(0, list_length):
        try:
            ovr = my_list_1[d] / my_list_2[d]
        except TypeError:
            print("wrong type")
            ovr = 0
        except (ZeroDivisionError, ValueError):
            print("division by 0")
            ovr = 0
        except IndexError:
            print("out of range")
            ovr = 0
        finally:
            res.append(ovr)
    return (res)
