#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int) and idx < x:
                print("{:d}".format(my_list[i]), end='')
                idx += 1
        except TypeError:
            continue
    print()
    return idx
