#!/usr/bin/python3
"""Log parsing script that reads stdin and prints metrics."""

import sys

total_size = 0
line_count = 0

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 2:
            continue

        status = parts[-2]
        size = parts[-1]

        if status in status_codes:
            status_codes[status] += 1

        try:
            total_size += int(size)
        except ValueError:
            pass

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
