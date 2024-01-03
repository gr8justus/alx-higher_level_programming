#!/usr/bin/python3
"""Print the letters of the English alphabet"""
for letter in range(ord("a"), ord("z") + 1):
    print(chr(letter), end="")
