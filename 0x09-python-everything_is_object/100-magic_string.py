#!/usr/bin/python3
def magic_string():
    magic_string.repet_count = getattr(magic_string, 'repet_count', 0) + 1
    return "BestSchool" * magic_string.repet_count
