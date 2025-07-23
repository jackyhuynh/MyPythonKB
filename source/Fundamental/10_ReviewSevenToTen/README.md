# Programming Fundamentals I - Exam 3 Review

This review covers topics from Chapters 7, 8, 9, and 10, focusing on concepts related to object-oriented programming,
data structures (lists, tuples, dictionaries), and string manipulation in Python.

## I. Object-Oriented Programming (OOP) Concepts

1. Mutator methods are also known as: What is their purpose in a class?
2. Which method is automatically called when you pass an object as an argument to the print function?
3. What can be thought of as a self-contained unit that consists of data attributes and the methods that operate on the
   data attributes?
4. The procedures that an object performs are called?
5. What does the acronym UML stand for?
6. Which section in the UML holds the list of the class's data attributes?
7. What type of programming contains class definitions?
8. How do you create an object named worker_joey from a Worker class?
9. Practice: Write a setter/mutator method and a getter/accessor method for a private _book_title attribute within a
   Book class.

## II. Data Structures: Lists

1. Which method or operator can be used to concatenate lists?
2. Which method can be used to place an item at a specific index in a list?
3. When working with multiple sets of data, one would typically use a(n):
4. What will be the value of number after number = range(0, 9, 2) executes?
5. Given my_string = '03/07/2018' and list_strip = my_string.split('/'), what will list_strip reference?
6. Analyze the following code:

```python

list1 = [1, 2, 3]
list2 = []
for element in list1:
    list2.append(element)
    list1 = [4, 5, 6]
```

What will be the value of list2 after this code executes?

7. Practice:
    - Assume authors references a list. Write a for loop that displays each author in the list.
    - Write a function definition for list_total that accepts a list of integers, sums them, and returns the total.

## III. Data Structures: Tuples

1. What is an advantage of using a tuple rather than a list?
2. Which method can be used to convert a list to a tuple?
3. Which method can be used to convert a tuple to a list?
4. Practice:
    - Assume our_tuple references a tuple. Write a statement that converts it to a list called our_list.

## IV. Data Structures: Dictionaries

1. Which method would you use to get all the elements in a dictionary returned as a list of tuples?
2. Which function would you use to get the number of elements in a dictionary?
3. Analyze the following code:

```aiignore
cities = {'GA': 'Atlanta', 'NY': 'Albany', 'CA': 'San Diego'}
if 'CA' in cities:
del cities['CA']
cities['CA'] = 'Sacramento'
print(cities)
```

What will be displayed after this code executes? (Note: the order of dictionary entries may vary.)

5. Practice:
    - Assume definitions references a dictionary. Write an if statement that checks if the key 'marsupial' exists. If it
      does,
      delete it and its value. Otherwise, display a message indicating it's not in the dictionary.

## V. String Manipulation

1. What will be assigned to s_string after special = '1357 Country Ln.' and s_string = special[:4] executes?
2. What will be displayed after the following code executes?

```python 
mystr = 'yes'
yourstr = 'no'
mystr += yourstr * 2
print(mystr)
```

3. What will be assigned to some_nums after special = '0123456789' and some_nums = special[0:10:2] executes?
4. Practice:
    - Assume big references a string. Write a statement that converts the string it references to lowercase and assigns
      the
      converted string to the variable little.
    - Write Python code that asks the user to enter a series of single-digit numbers without separation (e.g., "2514").
      The
      program should then display the sum of these digits.

## VI. File Handling
What is the process used to convert an object to a stream of bytes that can be saved in a file?