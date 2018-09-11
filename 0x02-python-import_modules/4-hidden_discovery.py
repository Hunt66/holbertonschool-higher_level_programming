#!/usr/bin/python3
import dis
import hidden_4
lst = dir(hidden_4)
lst.sort()
for i in range(len(lst)):
    str = lst[i]
    if str[:2] != '__':
        print(str)
