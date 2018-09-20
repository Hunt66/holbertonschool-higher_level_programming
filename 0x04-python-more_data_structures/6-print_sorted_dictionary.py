#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    klist = a_dictionary.keys()
    keylist = list(klist)
    keylist.sort()
    for i in keylist:
        print("{:s}: {}".format(i, a_dictionary[i]))
