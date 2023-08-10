#!/usr/bin/python3
"""Return an int of fewest moves needed to result in
   exactly n H
"""


def minOperations(n):
    """Calculate fewest number of operations needed to
       result in exactly n H chars in the file"""
    result = 0
    paste = 2
    if isinstance(n, int) and n < 2:
        return 0
    while paste < n + 2:
        if n % paste == 0:
            result += paste
            n //= paste
            paste = 2
        else:
            paste += 1
    return result
