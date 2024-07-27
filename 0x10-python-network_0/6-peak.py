#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in the list.
    A peak element is one that is greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None

    def find_peak_util(start, end):
        mid = (start + end) // 2

        # Check if mid element is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the left neighbor is greater, then there must be a peak in the left half
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return find_peak_util(start, mid - 1)

        # If the right neighbor is greater, then there must be a peak in the right half
        return find_peak_util(mid + 1, end)

    return find_peak_util(0, len(list_of_integers) - 1)
