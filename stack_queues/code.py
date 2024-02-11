#!/usr/bin/python3

from unicodedata import lookup
[lookup('WHITE' + s.upper() + 'SUIT') for s in SUITS]
