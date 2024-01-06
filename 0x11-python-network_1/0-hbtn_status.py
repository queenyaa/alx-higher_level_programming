#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
