#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as _err_or:
        print("Exception: {}".format(_err_or), file=sys.stderr)
        return False
    else:
        return True
