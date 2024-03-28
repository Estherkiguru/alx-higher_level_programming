#!/bin/bash
#takes in URL,displays HTTP methods server accepts
curl -sI ALLOW $1 -L | grep "ALLOW" | cut -d " " -f2-
