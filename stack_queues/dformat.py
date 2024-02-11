#!/usr/bin/python3
"""
The Object Metaphor
"""
from datetime import date
sun = date(2024, 2, 11)
print(date(2024, 2, 11) - sun)
print(sun.year)
print(sun.month)
print(sun.day)
print(sun.strftime('%A, %B %d'))
