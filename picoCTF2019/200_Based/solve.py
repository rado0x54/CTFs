#!/usr/bin/env python3

import re
from pwn import remote

r = remote('jupiter.challenges.picoctf.org', 29221)

# Binary
binary_raw = r.recvuntil(b'Input:').decode()
p = re.compile('.*Please give the (.*) as a word.*', re.DOTALL)
binary_chars = p.match(binary_raw).group(1).split()
word = bytes([int(bc, 2) for bc in binary_chars]).decode()
r.sendline(word)

# Oct
binary_raw = r.recvuntil(b'Input:').decode()
p = re.compile('.*Please give me the  (.*) as a word.*', re.DOTALL)
oct_chars = p.match(binary_raw).group(1).split()
word = bytes([int(oc, 8) for oc in oct_chars]).decode()
r.sendline(word)

# Hex
binary_raw = r.recvuntil(b'Input:').decode()
p = re.compile('.*Please give me the (.*) as a word.*', re.DOTALL)
hex_chars = p.match(binary_raw).group(1)
word = bytearray.fromhex(hex_chars).decode()
print(word)
r.sendline(word)

binary_raw = r.recvall().decode()
p = re.compile('.*Flag: (picoCTF{.*}).*', re.DOTALL)
flag = p.match(binary_raw).group(1)

print(flag)
# picoCTF{learning_about_converting_values_00a975ff}
