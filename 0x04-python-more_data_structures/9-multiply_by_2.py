#!/usr/bin/python3
def multiply_by_2(a_dict):
    tmp_dict = a_dict.copy()
    for x in tmp_dict.keys():
        tmp_dict[x] *= 2
    return (tmp_dict)
