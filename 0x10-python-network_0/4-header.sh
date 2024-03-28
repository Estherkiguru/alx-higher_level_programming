#!/bin/bash
#takes an URL as argument,sends GET reques,displays response bopdy
curl -s "$1" -H "X-School-User-Id: 98"
