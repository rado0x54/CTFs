#!/usr/bin/env python3

CIPHERTEXT = 'dspttjohuifsvcjdpoabrkttds'
# (ord(K) - ord('a')) + {1-25} % 26 = ord(C)


def move(c_char, shift):
    return chr(((ord(c_char) - ord('a')) + shift) % 26 + ord('a'))


# test all solutions. only 25 makes sense
print(f"picoCTF{{{''.join([move(c, 25) for c in CIPHERTEXT])}}}")
