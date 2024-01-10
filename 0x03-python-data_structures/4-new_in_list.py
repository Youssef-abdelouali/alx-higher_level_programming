#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list[:]
    if 0 <= idx < len(my_list):
        copied_list[idx] = element
        return copied_list
    return my_list
