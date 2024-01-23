#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    np = 0
    for n in range(x):
        try:
            np += 1
        except IndexError:
            break
    print()
    return np
