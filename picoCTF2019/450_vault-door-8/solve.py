#!/usr/bin/env python3

EXPECTED_SCRAMBLED = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4,
0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC2, 0xD2, 0x95, 0xA4, 0xF0, 0xD2, 0xD2, 0xC1, 0x95]


# Scramble algorithm changes bits in the following way:
# IN : 76543210
# OUT: 54107632

def unscrambleByte(sb):
    out = 0x00
    out |= (sb & 0b00000001) << 2
    out |= (sb & 0b00000010) << 2
    out |= (sb & 0b00000100) << 4
    out |= (sb & 0b00001000) << 4
    out |= (sb & 0b00010000) >> 4
    out |= (sb & 0b00100000) >> 4
    out |= (sb & 0b01000000) >> 2
    out |= (sb & 0b10000000) >> 2
    return chr(out)


PASSWORD = ''.join(unscrambleByte(b) for b in EXPECTED_SCRAMBLED)
print(f"picoCTF{{{PASSWORD}}}")
# picoCTF{s0m3_m0r3_b1t_sh1fTiNg_89eb3994e}
