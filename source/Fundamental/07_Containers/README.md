## Chapter 7: Lists and Tuples

In previous chapters, we've dealt primarily with single pieces of data. However, real-world problems often involve
collections of data. Python provides powerful **data structures** to organize and manipulate these collections
efficiently. This chapter introduces you to two fundamental sequence data structures: **lists** and **tuples**.

### 1\. Introduction to Lists

A **list** is a versatile and commonly used data structure in Python. It's an ordered, mutable (changeable) collection
of items. This means you can add, remove, or modify elements after the list has been created. Lists can hold items of
different data types (e.g., numbers, strings, even other lists\!).

* **Creating and using lists**: Lists are defined by enclosing comma-separated items within square brackets `[]`.

```python
# Creating empty lists
empty_list = []
another_empty_list = list()

# Creating lists with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_data = ["Alice", 25, 1.75, True]
```

* **Accessing list elements**:

    * Elements in a list are accessed by their **index**, which is their position in the list. Python uses **zero-based
      indexing**, meaning the first element is at index 0, the second at index 1, and so on.
    * You can also use negative indices to access elements from the end of the list (`-1` for the last item, `-2` for
      the second to last, etc.).

  <!-- end list -->

```python
my_list = ["a", "b", "c", "d", "e"]
print(my_list[0])  # Output: a (first element)
print(my_list[2])  # Output: c (third element)
print(my_list[-1])  # Output: e (last element)
print(my_list[-3])  # Output: c (third from last)
```

* **Modifying list elements**: Since lists are mutable, you can change the value of an element by assigning a new value
  to its index.

```python
scores = [85, 92, 78, 95]
scores[1] = 88  # Change the second score (at index 1)
print(scores)  # Output: [85, 88, 78, 95]
```

### 2\. List Methods and Functions

Python provides a rich set of built-in methods (functions that belong to list objects) and functions that work with
lists.

* **Common list methods**:

    * `append(item)`: Adds an item to the end of the list.
    * `insert(index, item)`: Inserts an item at a specific index.
    * `remove(value)`: Removes the first occurrence of a specified value. Raises `ValueError` if the value is not found.
    * `pop([index])`: Removes and returns the item at a given index (defaults to the last item).
    * `sort()`: Sorts the list in ascending order (in-place modification).
    * `reverse()`: Reverses the order of elements in the list (in-place modification).
    * `count(value)`: Returns the number of times a value appears in the list.
    * `index(value)`: Returns the index of the first occurrence of a value. Raises `ValueError` if the value is not
      found.
    * `clear()`: Removes all items from the list.

  <!-- end list -->

```python
my_shopping_list = ["milk", "bread"]
my_shopping_list.append("eggs")  # ['milk', 'bread', 'eggs']
my_shopping_list.insert(0, "yogurt")  # ['yogurt', 'milk', 'bread', 'eggs']
my_shopping_list.remove("bread")  # ['yogurt', 'milk', 'eggs']
last_item = my_shopping_list.pop()  # 'eggs' (list is now ['yogurt', 'milk'])
print(my_shopping_list)

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # [1, 1, 2, 3, 4, 5, 9]
numbers.reverse()  # [9, 5, 4, 3, 2, 1, 1]
print(numbers.count(1))  # 2
```

* **Using functions like `len()`, `min()`, `max()`, and `sum()` with lists**:

    * `len(list)`: Returns the number of items in a list.
    * `min(list)`: Returns the smallest item in a list.
    * `max(list)`: Returns the largest item in a list.
    * `sum(list)`: Returns the sum of all numeric items in a list.

  <!-- end list -->

```python
data = [10, 20, 30, 40, 50]
print(len(data))  # Output: 5
print(min(data))  # Output: 10
print(max(data))  # Output: 50
print(sum(data))  # Output: 150
```

### 3\. Working with Lists

* **Iterating over lists using loops**: The `for` loop is the most common and Pythonic way to process each item in a
  list.

```python
students = ["Anna", "Ben", "Carla"]
for student in students:
    print(f"Hello, {student}!")

# Iterating with index (using enumerate)
for index, student in enumerate(students):
    print(f"Student {index + 1}: {student}")
```

* **List slicing**: You can extract a portion (a "slice") of a list to create a new list. This is done using colon `:`
  notation within square brackets.

```python
my_numbers = [10, 20, 30, 40, 50, 60]
print(my_numbers[1:4])  # Output: [20, 30, 40] (from index 1 up to, but not including, index 4)
print(my_numbers[:3])  # Output: [10, 20, 30] (from beginning up to index 3)
print(my_numbers[2:])  # Output: [30, 40, 50, 60] (from index 2 to the end)
print(my_numbers[::2])  # Output: [10, 30, 50] (every second element)
print(my_numbers[::-1])  # Output: [60, 50, 40, 30, 20, 10] (reverse the list)
```

* **List comprehensions**: A concise way to create new lists from existing iterables. They often provide a more readable
  and efficient alternative to `for` loops for list creation.

```python
# Using a for loop to create a list of squares
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# Equivalent list comprehension
squares_comp = [x ** 2 for x in range(1, 6)]
print(squares_comp)  # Output: [1, 4, 9, 16, 25]

# List comprehension with a condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

### 4\. Tuples

A **tuple** is similar to a list in that it's an ordered collection of items. However, the key difference is that tuples
are **immutable**, meaning once a tuple is created, its elements cannot be changed, added, or removed.

* **Understanding tuples and their immutability**:

    * Immutability makes tuples useful for data that should not change (e.g., coordinates, configurations, database
      records that shouldn't be altered).
    * Tuples are often used when you need to ensure data integrity.
    * They are also slightly more memory-efficient and faster to process than lists.

* **Creating and using tuples**: Tuples are defined by enclosing comma-separated items within parentheses `()`.
  Parentheses are optional if there's no ambiguity, but highly recommended for readability, especially for empty or
  single-element tuples.

```python
# Creating tuples
empty_tuple = ()
single_item_tuple = (1,)  # Comma is required for single-item tuples
coordinates = (10.0, 20.5)
employee_record = ("John Doe", "Marketing", 55000)

# Accessing tuple elements (same as lists, by index)
print(coordinates[0])  # Output: 10.0
print(employee_record[1])  # Output: Marketing

# Attempting to modify (will raise an error)
# employee_record[0] = "Jane Doe" # TypeError: 'tuple' object does not support item assignment
```

### 5\. List and Tuple Operations

Many operations that work with sequences apply to both lists and tuples:

* **Concatenation**: Use the `+` operator to combine two lists or two tuples. This creates a *new* list/tuple.

```python
list1 = [1, 2]
list2 = [3, 4]
combined_list = list1 + list2  # [1, 2, 3, 4]

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2  # (1, 2, 3, 4)
```

* **Repetition**: Use the `*` operator to repeat a list or tuple multiple times.

```python
repeated_list = [0] * 5  # [0, 0, 0, 0, 0]
repeated_tuple = ("hi",) * 3  # ('hi', 'hi', 'hi')
```

* **Membership testing**: Use the `in` and `not in` operators to check if an item exists within a list or tuple.

```python
fruits = ["apple", "orange"]
print("apple" in fruits)  # True
data = [10, 20, 50]
print(50 not in data)  # False
```

* **Min, Max, Sum, Len**: As seen, `len()`, `min()`, `max()`, and `sum()` also work for tuples.

* **Converting between lists and tuples**:

    * You can convert a list to a tuple using the `tuple()` constructor.
    * You can convert a tuple to a list using the `list()` constructor.

  <!-- end list -->

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)

my_tuple2 = ("a", "b", "c")
my_list2 = list(my_tuple2)  # ['a', 'b', 'c']
```