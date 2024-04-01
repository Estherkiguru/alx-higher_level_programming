#!/usr/bin/python3
"""
takes in URLsends request,displays response body
"""


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
