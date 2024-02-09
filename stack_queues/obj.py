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
>>> suits[0:2] = ['heart', 'diamond']
>>> suits
>>> chinese

"""
chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
print(suits)
print(chinese)
import doctest
doctest.testmod()
