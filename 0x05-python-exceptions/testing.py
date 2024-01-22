#!/usr/bin/python3

while True:
    try:
        x = int(input('enter a number: '))
        break
    except ValueError:
        print('Oops! invalid number')
