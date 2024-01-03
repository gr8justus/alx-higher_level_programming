#!/usr/bin/python3
"""Print the letters of the English alphabet"""
for letter in range(ord("a"), ord("z") + 1):
    letter = chr(letter)
    if letter == "e" or letter == "q":
        continue
    else:
        print("{}".format(letter), end='')
