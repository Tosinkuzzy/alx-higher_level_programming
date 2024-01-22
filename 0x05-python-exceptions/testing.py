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
try:
    raise Exception ('spam', 'Eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    z = x, y
    print('x =', x)
    print('y =', y)
    print('z =', z * 3)
except ValueError:
    print('z =', z)
