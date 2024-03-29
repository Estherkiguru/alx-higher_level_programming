#!/usr/bin/python3
"""
takes in a URL,sends request to URL,displays value of X-Request-Id
"""

import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id')
