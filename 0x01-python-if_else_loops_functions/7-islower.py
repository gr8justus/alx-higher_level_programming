#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase"""
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return 1
    else:
        return 0
