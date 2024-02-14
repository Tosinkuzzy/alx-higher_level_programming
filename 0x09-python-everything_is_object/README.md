
0x09. Python - Everything is object
Python
OOP
 By: Guillaume
 Weight: 1
 Project over - took place from Jan 30, 2024 6:00 AM to Jan 31, 2024 6:00 AM
 An auto review will be launched at the deadline

Background Context
Now that we understand that everything is an object and have a little bit of knowledge, 
let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
OK. But what about this?

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 

