#!/usr/bin/env python3

INPUT_INTS = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734291511, 960049251, 1681089078]
PASSWORD_BYTES = b''.join([i.to_bytes(4, byteorder='big') for i in INPUT_INTS])
print(f"picoCTF{{{PASSWORD_BYTES.decode()}}}")

