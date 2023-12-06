#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    tot_sum = 0

    for arg in argv[1:]:
        tot_sum += int(arg)
    print(tot_sum)
