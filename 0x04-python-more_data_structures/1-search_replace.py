#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_element(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_element, my_list))
