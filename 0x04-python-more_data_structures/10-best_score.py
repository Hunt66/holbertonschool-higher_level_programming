#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = a_dictionary[next(iter(a_dictionary))]
    for i in a_dictionary:
        if a_dictionary[i] > score:
            score = a_dictionary[i]
            ans = i
    return ans
