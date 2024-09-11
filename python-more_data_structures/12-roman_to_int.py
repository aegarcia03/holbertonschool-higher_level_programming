#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    last = 'I'

    for i in roman_string[::-1]:
        if roman_num[i] < roman_num[last]:
            result -= roman_num[i]
        else:
            result += roman_num[i]
        last = i

    return result
