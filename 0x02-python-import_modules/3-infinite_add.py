#!/usr/bin/python3
import sys
args = sys.argv[1:]
count = len(args)
sum = 0
for i in range(count):
    sum = sum + int(args[i])
print(sum)
