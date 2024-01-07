#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: list to retrieve element from
        idx: element index

    Return:
        element at idx
    """
    max_index = len(my_list) - 1

    if idx < 0 or idx > max_index:
        return None

    return my_list[idx]
