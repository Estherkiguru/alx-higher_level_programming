#!/bin/bash
#takes in URL,displays HTTP methods server accepts
curl -sI "$1" | grep -i Allow | awk '{print $2,$3,$4}'
