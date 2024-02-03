#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    i = 0

    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            idx += 1
            i += 1
        except IndexError:
            print()
            return i
        except Exception:
            idx += 1

    print()
    return i
