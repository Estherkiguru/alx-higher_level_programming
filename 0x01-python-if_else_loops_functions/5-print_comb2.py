#!/usr/bin/python3
for i in range(0, 99 + 1):
    print("{:02}".format(i), end="," if i < 99 else "\n")
