#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    for i in range(len(a)):
        if a[i] == C or a[i] == c:
            a[i] = ""
    return "".join(a)
