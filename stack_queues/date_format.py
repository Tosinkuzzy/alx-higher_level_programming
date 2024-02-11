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
sun = date(2014, 5, 13)
print(date(2014, 5, 19) - sun)
sun.year
sun.strftime('%A, %B %d')
