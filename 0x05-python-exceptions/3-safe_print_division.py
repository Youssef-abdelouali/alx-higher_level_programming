#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        _division_ = a / b
    except (TypeError, ZeroDivisionError):
        _division_ = None
    finally:
        print("Inside result: {}".format(_division_))
    return (_division_)
