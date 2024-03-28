#!/bin/bash
#sends JSON POST request to URL,displays the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
