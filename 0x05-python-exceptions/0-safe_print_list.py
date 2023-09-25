#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    cnt = 0 #initialize a counter to keep track of elements printed

    for d in range(x):
        try:
        # for d in range(x):
            print("{}".format(my_list[cnt]), end="")   #print without new line
            cnt += 1
            # x -= 1
        except IndexError:
            pass    #handle case where index is out of range

        """
        except Exception:
            print("Catch all")
        finally:
            print("")
        """
    print() print newline char to separate the output
    return (cnt)
