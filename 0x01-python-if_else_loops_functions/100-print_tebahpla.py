#!/usr/bin/python3
for ascii_val in range(ord('z'), ord('a') - 1, -1):
    if ascii_val % 2 == 0:
        off_set = 0
    else:
        off_set = 32
    print('{}'.format(chr(ascii_val - off_set)), end='')
