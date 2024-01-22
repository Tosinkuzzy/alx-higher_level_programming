#!/usr/bin/python3

while True:
    try:
        x = int(input('enter a number: '))
        break
    except ValueError:
        print('Oops! invalid number')

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
            raise cls()
    except B:
        print('B')
    except C:
        print('C')
    except D:
        print('D')

