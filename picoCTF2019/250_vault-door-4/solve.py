#!/usr/bin/env python3

ints_0_8 = [106, 85, 53, 116, 95, 52, 95, 98]
hex_8_16 = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
oct_16_24 = [0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o143, 0o61]
char_24_32 = ['9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']

ints_0_8_str = ''.join([chr(o) for o in ints_0_8])
hex_8_16_str = ''.join([chr(o) for o in hex_8_16])
oct_16_24_str = ''.join([chr(o) for o in oct_16_24])
char_24_32_str = ''.join(char_24_32)

print(f"picoCTF{{{ints_0_8_str + hex_8_16_str + oct_16_24_str + char_24_32_str}}}")
