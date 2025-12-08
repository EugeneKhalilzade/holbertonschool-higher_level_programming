#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for index, value in enumerate(my_list):
        if search == value:
            new_list[index] = replace
    return new_list
