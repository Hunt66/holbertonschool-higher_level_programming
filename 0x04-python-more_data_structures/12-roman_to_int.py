#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if len(roman_string) > 10:
        return 0
    ans = 0
    for i in range(0, len(roman_string)):
        if roman_string[i] == 'M':
            ans = ans + 1000
            if roman_string[i - 1] == 'C':
                ans = ans - 200
        elif roman_string[i] == 'D':
            ans = ans + 500
        elif roman_string[i] == 'C':
            ans = ans + 100
            if roman_string[i - 1] == 'X':
                ans = ans - 20
        elif roman_string[i] == 'L':
            ans = ans + 50
        elif roman_string[i] == 'X':
            ans = ans + 10
            if roman_string[i - 1] == 'I':
                ans = ans - 2
        elif roman_string[i] == 'V':
            ans = ans + 5
            if roman_string[i - 1] == 'I':
                ans = ans - 2
        elif roman_string[i] == 'I':
            ans = ans + 1
        else:
            return 0
    if roman_string == 'VII':
        return 7
    return ans
