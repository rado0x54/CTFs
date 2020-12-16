#!/usr/bin/env python3

import re
from pwn import remote

r = remote('jupiter.challenges.picoctf.org', 64287)

payload = str(r.recvall())
m = re.search(r"(picoCTF{\S*})", payload)
print(m.group(0))
# picoCTF{nEtCat_Mast3ry_284be8f7}
