#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
        Print x elements of my_list
    """
    print_count = 0  # keeps track of elements printed

    try:
        for index in range(x):
            print(my_list[index], end="")
            print_count += 1
    except IndexError:
        print()
    else:
        print()  # prints a new line before prompt

    return print_count
