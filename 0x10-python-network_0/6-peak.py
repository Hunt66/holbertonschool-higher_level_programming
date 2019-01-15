#!/usr/bin/python3
""" finds a peak in a list of unsorted ints """


def find_peak(list_of_integers):
    """ finds the peak int or none if no list """
    if len(list_of_integers) == 0:
        return None
    else:
        return max(list_of_integers)
