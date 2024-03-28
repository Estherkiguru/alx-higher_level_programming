#!/bin/bash
#takes in a URL,sends request to URL,displays body of response
curl -s "$1" -X GET -L
