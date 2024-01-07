0x03. Python - Data Structures: Lists, Tuples
Python
 By: Guillaume
 Weight: 1
 Project will start Jan 5, 2024 6:00 AM, must end by Jan 9, 2024 6:00 AM
 Checker was released at Jan 6, 2024 6:00 AM

[Resources]
Read or watch:

3.1.3. Lists
Data structures (until 5.3. Tuples and Sequences included)
Learn to Program 6 : Lists

[Learning Objectives]
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

{General}
Why Python programming is awesome
What are lists and how to use them
What are the differences and similarities between strings and lists
What are the most common methods of lists and how to use them
How to use lists as stacks and queues
What are list comprehensions and how to use them
What are tuples and how to use them
When to use tuples versus lists
What is a sequence
What is tuple packing
What is sequence unpacking
What is the del statement and how to use it.

Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

{Requirements}:
[Python Scripts]:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

[C]:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
You are not allowed to use global variables
No more than 5 functions per file
In the following examples, the main.c files are shown as examples. 
You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account).
We will use our own main.c files at compilation. 
Our main.c files might be different from the one shown in the examples
The prototypes of all your functions should be included in your header file called lists.h
Don’t forget to push your header file
All your header files should be include guarded.

[QUIZ QUESTIONS]:

Question #0
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> b
a
output = [1, 2, 3, 4]

Question #1
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
b
output = [1, 2, 10, 4]

Question #2
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a
b
output = [1, 2, 10, 4]

Question #3
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
output = [1, 2, 10, 4]

Question #4
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[0]
output = 1

Question #5
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> len(a)
output = 4

Question #6
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[-1]
output = 4

Question #7
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[1:3]
output = [2, 3]
