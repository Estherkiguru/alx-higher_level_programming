#!/usr/bin/python3
"""
takes in a URL,sends request to URL,displays value of X-Request-Id
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
