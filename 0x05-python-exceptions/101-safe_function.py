#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        res_ult = fct(*args)
        return res_ult
    except Exception as exce_p:
        print("Exception: {}".format(exce_p), file=sys.stderr)
        return None
