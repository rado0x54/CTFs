#!/usr/bin/env python3

KEY = 'SOLVECRYPTO'
CIPHERTEXT = 'UFJKXQZQUNB'

# Substituion Table shifts Input by ord(K) - ord('A'): 'A' -> 0, 'B' -> 1 etc
# (ord(K) - ord('A')) + (ord(K) - ord('A')) % 26 = ord(C)


def reverse(c_char, k_char):
    return chr(((ord(c_char) - ord('A')) - (ord(k_char) - ord('A'))) % 26 + ord('A'))


print(f"picoCTF{{{''.join([reverse(c, k) for k, c in zip(KEY, CIPHERTEXT)])}}}" )
