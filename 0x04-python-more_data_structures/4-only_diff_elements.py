#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for i in set_1:
        if i not in set_2:
            set_3.add(i)
    for i in set_2:
        if i not in set_1 and i not in set_3:
            set_3.add(i)
    return set_3
