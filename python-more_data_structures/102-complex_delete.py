#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    removed_keys = []
    for key, val in a_dictionary.items():
        if val == value:
            removed_keys.append(key)
    for i in removed_keys:
        a_dictionary.pop(i)
    return a_dictionary
