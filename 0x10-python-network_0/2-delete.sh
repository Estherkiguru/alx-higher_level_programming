#!/bin/bash
#sends DELETE request to URL passed as first argument,displays response
curl -sX DELETE $1 -L
