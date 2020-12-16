#!/usr/bin/env python3

import re
p = re.compile(r'password.charAt\((\d+)\)\s+== \'(.)\'')

password_lines = [line.strip() for line in open('VaultDoor1.java') if 'password.charAt' in line]
sorted_pos_char_list = sorted([p.match(line).groups() for line in password_lines], key=lambda x: int(x[0]))

print(f'picoCTF{{{"".join([x[1] for x in sorted_pos_char_list])}}}')
# picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
