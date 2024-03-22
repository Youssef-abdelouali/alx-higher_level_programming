#!/usr/bin/python3
def complex_delete(my_dict, value):
    copy_dict = my_dict.copy()
    for key, val in copy_dict.items():
        if value == val:
            my_dict.pop(key)
    return my_dict
