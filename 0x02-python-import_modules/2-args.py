#!/usr/bin/python3
from sys import argv
argc = len(argv)
print("{:d} arguments:".format(argc - 1))
if argc > 0:
    for index in range(1, argc):
        if __name__ == "__main__":
            print("{:d}: {}".format(index, argv[index]))
