#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    np = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end='')
            np += 1
        except (ValueError, TypeError):
            continue

    print()
    return np
