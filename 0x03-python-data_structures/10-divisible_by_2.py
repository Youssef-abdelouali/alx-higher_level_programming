#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = my_list[:]
    for index, element in enumerate(my_list):
        if element % 2 == 0:
            result_list[index] = True
        else:
            result_list[index] = False
    return result_list
