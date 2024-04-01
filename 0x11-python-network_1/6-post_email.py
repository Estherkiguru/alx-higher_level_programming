#!/usr/bin/python3
"""
takes in URL and email, sends POST request, displays response body
"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}
    response = requests.post(url, data=payload)
    print(response.text)
