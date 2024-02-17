#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(si_ze, status_code):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(si_ze))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    si_ze = 0
    status_code = {}
    valid_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    count_line = 0

    try:
        for line in sys.stdin:
            if count_line == 10:
                print_stats(si_ze, status_code)
                count_line = 1
            else:
                count_line += 1

            line = line.split()

            try:
                si_ze += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_code:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(si_ze, status_code)

    except KeyboardInterrupt:
        print_stats(si_ze, status_code)
        raise
