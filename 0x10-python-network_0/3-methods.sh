#!/bin/bash
#takes in URL,displays HTTP methods server accepts
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
