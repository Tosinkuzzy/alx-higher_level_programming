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

Question #8
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
output = 5

Question #9
What do these lines print?

>>> a = [1, 2, 3, 4]
>>> a[-3]
output = 2

[Tasks]:
0. Print a list of integers
mandatory
Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 0-print_list_integer.py

1. Secure access to an element in a list
mandatory
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 1-element_at.py

2. Replace element
mandatory
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 2-replace_in_list.py

3. Print a list of integers... in reverse!
mandatory
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 3-print_reversed_list_integer.py

4. Replace in a copy
mandatory
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 4-new_in_list.py
