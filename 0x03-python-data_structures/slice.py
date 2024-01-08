#!/usr/bin/python3
a = [1, 5, 8, 4, 5, 10]
b = a[-4]
c = a
c.append(15)
c.sort()
del c[-2]
print(c)
print(b)
