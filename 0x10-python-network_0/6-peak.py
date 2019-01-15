#!/usr/bin/python3
""" finds a peak in a list of unsorted ints """


def find_peak(list_of_integers):
    """ finds the highest int or none if no list """
    if len(list_of_integers) == 0:
        return None
    else:
        max = list_of_integers[0]
        for i in list_of_integers:
            if max < i:
                max = i
        return max
