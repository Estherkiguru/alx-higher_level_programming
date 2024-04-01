#!/usr/bin/python3
"""
takes in a letter,sends POST request to http://0.0.0.0:5000/search_user
"""


import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = " "

    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                  json_response.get('name')))

        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
