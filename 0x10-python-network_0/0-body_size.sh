#!/bin/bash
#Bash script that takes in a URL and sends a request to that URL
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
