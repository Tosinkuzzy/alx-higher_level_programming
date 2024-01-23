#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for n in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("Wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            nl.append(result)
        return nl
