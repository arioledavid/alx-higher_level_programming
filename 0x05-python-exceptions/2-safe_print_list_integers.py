#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    printed = 0
    while True:
        try:
            if idx < x:
                print("{}".format(my_list[idx]), end="")
                idx += 1
                printed += 1
            else:
                print()
                return printed
        except(ValueError, TypeError):
            idx += 1

