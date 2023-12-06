#!/usr/bin/python3
import string
print(*getattr(string, '_'.join(['ascii', 'uppercase'])), sep='')
