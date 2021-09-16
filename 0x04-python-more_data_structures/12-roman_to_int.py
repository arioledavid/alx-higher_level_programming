#!/usr/bin/python3
def roman_to_int(roman_string):
    value = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    #initialize previous character and answer
    p = 0
    ans = 0
    #Transverse through a
    n = len(roman_string)
    for i in range(n-1, -1, -1):
        #if greater than or equal to previous,
        #add to answer
        if value[roman_string[i]] >= p:
            ans += value[roman_string[i]]
        #if smaller than previous
        else:
            ans -= value[roman_string[i]]
        #update previous
        p = value[roman_string[i]]
    return(ans)
