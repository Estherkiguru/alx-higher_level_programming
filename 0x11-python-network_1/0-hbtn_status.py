#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request


url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()

print(html)
