#!/usr/bin/python3
"""
takes in URL,sends request,displays response's body:Handles HTTP Error
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
