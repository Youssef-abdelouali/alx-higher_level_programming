#!/usr/bin/env python3
"""
This script reads input from standard input and computes metrics.
After every ten lines or when interrupted (CTRL + C),
it prints the following statistics:
- Total file size up to that point.
- Count of read status codes up to that point.
"""

import sys


def print_metrics(file_size, status_codes):

    """Print accumulated metrics."""
    print("File size: {}".format(file_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    file_size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    lines_read = 0

    try:
        for line in sys.stdin:
            if lines_read == 10:
                print_metrics(file_size, status_codes)
                lines_read = 1
            else:
                lines_read += 1

            data = line.split()

            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = data[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

        print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise
