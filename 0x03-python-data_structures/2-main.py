#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print_reversed_list_integer(my_list)
print(new_list)
print(my_list)
