#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element of a list copy

    Args:
        my_list: list
        idx: index of element to replace
        element: new value of element

    Returns:
        a copy of my_list
    """
    max_index = len(my_list) - 1

    if idx < 0 or idx > max_index:
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
