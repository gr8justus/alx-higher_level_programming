#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
        Print x elements, only integers
    """

    print_count = 0  # Keeps track of printed integers

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")  # Prints only integer
            print_count += 1
        except (TypeError, ValueError):
            pass

    print()  # Print a newline before prompt
    return print_count
