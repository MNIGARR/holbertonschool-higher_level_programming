#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]

    # Check invalid index
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Replace element at valid index
    new_list[idx] = element
    return new_list
