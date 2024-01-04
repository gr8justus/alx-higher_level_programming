#!/usr/bin/python3
from sys import argv
argc = len(argv)
if argc == 1:
    args = "arguments."
elif argc == 2:
    args = "argument:"
else:
    args = "arguments:"
if __name__ == "__main__":
    print("{:d} {}".format(argc - 1, args))
    if argc > 1:
        for index in range(1, argc):
            print("{:d}: {}".format(index, argv[index]))
