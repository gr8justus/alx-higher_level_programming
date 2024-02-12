#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
        Execute a function and handle exceptions
    """

    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    return result
