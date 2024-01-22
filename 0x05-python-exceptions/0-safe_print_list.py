#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print a specified number of elements from a list.

    Args:
        my_list (list): The list containing elements to be printed.
        x (int): The number of elements from my_list to print.

    Returns:
        int: The count of elements successfully printed.
    """
    track = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            track += 1
        except IndexError:
            break
    print("")
    return (track)
