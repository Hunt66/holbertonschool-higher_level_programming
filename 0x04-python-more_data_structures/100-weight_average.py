#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list[0] == None:
        return 0
    ans = 0.0
    div = 0.0
    for i in range(0, len(my_list)):
        ans += int(my_list[i][0]) * int(my_list[i][1])
    for i in range(0, len(my_list)):
        div += int(my_list[i][1])
    ans = ans / int(div)
    return ans
