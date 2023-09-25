#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    
    res = []
    
    try:
        for d in range(list_length):

            ele1 = my_list_1[d] if d < len(my_list_1) else 0
            ele2 = my_list_1[d] if d < len(my_list_2) else 0

            if isinstance(ele1, (int, float)) and isinstance(ele2, (int, float)):
                if ele2 == 0:
                    res.append(0)
                    print("division by 0")
                else:
                    res.append(ele1 / ele2)

            else:
                res.append(0)
                print("wrong type")
        
    except IndexError:
        print("out of range")
    finally:
        return (res)
