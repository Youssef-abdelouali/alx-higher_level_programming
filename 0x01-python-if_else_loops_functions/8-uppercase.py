#!/usr/bin/python3
def uppercase(str):
    for st in str:
        if ord(st) >= 97 and ord(st) <= 122:
            st = chr(ord(st) - 32)
        print("{}".format(st), end="")
    print()
