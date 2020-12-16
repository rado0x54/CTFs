#!/usr/bin/env python3

numbers = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']


def map_ord(c):
    return c if isinstance(c, str) else chr(ord('A') - 1 + c)


print("".join([map_ord(c) for c in numbers]))
