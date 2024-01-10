0x04. Python - More Data Structures: Set, Dictionary
[Python]:
 By: Guillaume
 Weight: 1
 Project will start Jan 10, 2024 6:00 AM, must end by Jan 11, 2024 6:00 AM
 Checker was released at Jan 10, 2024 12:00 PM

[Resources]:
[Read or watch]:

(Data structures)
(Lambda, filter, reduce and map)
(Learn to Program 12 Lambda Map Filter Reduce)
[man or help]:

[python3]:

Learning Objectives
[At the end of this project, you are expected to be able to explain to anyone, without the help of Google]:

[General]:
Why Python programming is awesome
What are sets and how to use them
What are the most common methods of set and how to use them
When to use sets versus lists
How to iterate into a set
What are dictionaries and how to use them
When to use dictionaries versus lists or sets
What is a key in a dictionary
How to iterate over a dictionary
What is a lambda function
What are the map, reduce and filter functions

[Copyright - Plagiarism]:
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

[Requirements]:

[General]:
[Allowed editors]: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

[Quiz questions]:

[Question]: #0
What do these lines print?

>>> for i in range(0, 3):
>>>     print(i, end=" ")

output = 0 1 2

[Question]: #1
What do these lines print?

>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")

output = 1 2 3 4

[Question]: #2
What do these lines print?

>>> for i in range(1, 4):
>>>     print(i, end=" ")

output = 1 2 3

[Question]: #3
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")

output = Amy

[Question]: #4
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a['id']

output = 89

[Question]: #5
What do these lines print?

>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")

output = 1 3 4 2

[Question]: #6
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)

output = 0

[Question]: #7
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')

output = 89

[Question]: #8
What do these lines print?

>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")

output = Hello Holberton School 98

[Question]: #9
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]

output = 4

[Question]: #10
What do these lines print?

>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')

output = [1, 2, 3, 4]

[Question]: #11
What do these lines print?

>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')

output = Nothing

[Tasks]:

0. Squared simple

Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc

guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[Repo]:

[GitHub repository]: alx-higher_level_programming
[Directory]: 0x04-python-more_data_structures
[File]: 0-square_matrix_simple.py
