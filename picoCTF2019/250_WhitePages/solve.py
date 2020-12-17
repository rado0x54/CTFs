#!/usr/bin/env python3

with open('whitepages.txt', "rb") as f:
    content = f.read()
    # replace pattern with '0' and '1'
    bin_str_content = content.replace(b'\xe2\x80\x83', b'0').replace(b'\x20', b'1').decode()
    char_content = [chr(int(bin_str_content[i:i+8], 2)) for i in range(0, len(bin_str_content), 8)]
    print(''.join(char_content))

# picoCTF{not_all_spaces_are_created_equal_c54f27cd05c2189f8147cc6f5deb2e56}
