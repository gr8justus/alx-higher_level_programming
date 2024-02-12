#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Prints integers only
    except (ValueError, TypeError) as err:
        # Print exception message to stderr
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
