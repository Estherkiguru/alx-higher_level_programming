#!/usr/bin/python3
"""
takes in URL,sends request to URL,displays X-Request-Id
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
