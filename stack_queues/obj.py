#!/usr/bin/python3

"""
Objects represent information and processes,
bundled together to represent the properties,
interactions, and behaviour of complex things.

>>> chinese = ['coin', 'string', 'myriad']
>>> suits = chinese
>>> suits.pop()
>>> suits.remove('string')
>>> suits.append('cup')
>>> suits.extend(['sword', 'club'])
>>> suits[2] = 'spade'
>>> suits
>>> chinese

"""
import doctest
doctest.testmod()
