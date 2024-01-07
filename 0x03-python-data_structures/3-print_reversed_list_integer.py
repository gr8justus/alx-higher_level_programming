#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print the items in a list in reverse

    Arg:
        my_list: list to print from
    """

    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
