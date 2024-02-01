#!/usr/bin/python3
"""
Using Basic Math API

to check if n > 0

if not to raise valueError("n must be >= 0")

if math floor parsing n != n 

raise valueErroe("n must be exact integer")

if n + 1 == n

raise OverflowError("n too large")

then output resut and factorial while 

checking if it's true or not

then we iterate throug fact and increment fact +1

return result
"""
import math
if not n >= 0:
    raise ValueError("n must be >= 0")
if math.floor(n) != n:
    raise ValueError("n must be exact integer")
if n + 1 == n:
    raise OverflowError("n too large")
result = 1
factorial = 2
while factorial <= n:
    result *= fact
    factorial += 1
return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
