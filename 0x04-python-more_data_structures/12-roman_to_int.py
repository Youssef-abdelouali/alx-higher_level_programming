#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    rom_da = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numb = [rom_da[x] for x in roman_string] + [0]
    roman_rep = 0

    for i in range(len(numb) - 1):
        if numb[i] >= numb[i+1]:
            roman_rep += numb[i]
        else:
            roman_rep -= numb[i]

    return roman_rep
