#!/usr/bin/env python3
"""Log parse statistics"""
import sys


def print_metrics(total_size, status_codes):
    """Print metrics"""
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == "__main__":
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    try:
        ln = 0
        for line in sys.stdin:
            line = line.split()
            file_size = line[-1]
            code = line[-2]
            total_size += int(file_size)
            if code in status_codes:
                ln += 1
                status_codes[code] += 1
                if ln % 10 == 0:
                    print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
    else:
        print_metrics(total_size, status_codes)
