#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_ave = 0
    den_ave = 0

    for tup_ave in my_list:
        num_ave += tup_ave[0] * tup_ave[1]
        den_ave += tup_ave[1]

    return (num_ave / den_ave)
