#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print the items in a list

    Arg:
        my_list: list to print from
    """

    for item in my_list:
        print("{:d}".format(item))
