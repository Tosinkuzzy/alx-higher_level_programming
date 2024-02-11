#!/usr/bin/python3

"""
    The Object Metaphor
    Specialized Object Syntax and associated
    Terminology
"""

"""
>>> from datetime import date
>>> sun = date(2024, 2, 11)
>>> print(date(2024, 2, 11) - sun)
>>> print(sun)

"""
from datetime import date
sun = date(2024, 2, 11)
print(date(2024, 2, 11) - sun)
print(sun.year)
print(sun.strftime('%A, %B %d'))
