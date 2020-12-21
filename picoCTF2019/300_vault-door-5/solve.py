#!/usr/bin/env python3

import base64
from urllib.parse import unquote

B64_ENCODED = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2'
URL_ENCODED = base64.b64decode(B64_ENCODED.encode()).decode()
print(f"picoCTF{{{unquote(URL_ENCODED)}}}")
