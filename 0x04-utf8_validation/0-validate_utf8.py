#!/usr/bin/python3
"""Validate utf-8 encoding
"""


def validUTF8(data):
    """Validate if data is valid UTF-8
    """
    # number of remaining bytes for UTF8 character completion (0-3)
    count = 0
    for byte in data:
        # if count ==0 then its a new UTF8 char
        # check most significant bits of byte and update if
        # bits match expectedUTF8 pattern
        if count == 0:
            if (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            elif (byte >> 7) != 0:
                return False
        # inside multi-byte UTF8 char
        # inner byte must start with 10 then decrease count
        # to match continuing bytes
        else:
            if (byte >> 6) != 0b10:
                return False
            else:
                count -= 1
    return (count == 0)
