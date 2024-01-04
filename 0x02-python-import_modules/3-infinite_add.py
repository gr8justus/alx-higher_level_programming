#!/usr/bin/python3
from sys import argv
argc = len(argv)
sum = 0
for index in range(1, argc):
    sum += int(argv[index])
print(sum)
