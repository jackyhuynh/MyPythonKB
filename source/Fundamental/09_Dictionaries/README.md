Here's the content for Chapters 9 through 15, following your detailed outline:

---

## Chapter 9: Dictionaries and Sets

This chapter introduces two more powerful and flexible built-in data structures in Python: dictionaries and sets. Both
offer unique ways to store and retrieve data efficiently.

### 1. Dictionaries

Dictionaries are unordered collections of *key-value pairs*. They are mutable, meaning their contents can be changed
after creation, and are highly optimized for retrieving values based on their keys. Think of a real-world dictionary
where you look up a word (the key) to find its definition (the value).

#### Creating and Using Dictionaries

Dictionaries are created using curly braces `{}` with key-value pairs separated by colons `:`. Each key-value pair is
separated by a comma. Keys must be immutable (e.g., strings, numbers, tuples), and unique within a dictionary. Values
can be of any data type.

**Creating a dictionary:**

```python
# Empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Dictionary with initial data
student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": {"math": 95, "physics": 88}  # Value can be another dictionary
}
print(student_info)
# Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'grades': {'math': 95, 'physics': 88}}
```

#### Accessing, Adding, Modifying, and Removing Key-Value Pairs

* **Accessing Values:** Values are accessed using their corresponding keys in square brackets `[]`.
    ```python
    print(student_info["name"])  # Output: Alice
    print(student_info["grades"]["math"]) # Output: 95
    # print(student_info["address"]) # This would raise a KeyError if 'address' doesn't exist
    ```

* **Adding New Key-Value Pairs:** New pairs are added by assigning a value to a new key.
    ```python
    student_info["city"] = "New York"
    print(student_info)
    # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'grades': {'math': 95, 'physics': 88}, 'city': 'New York'}
    ```

* **Modifying Values:** Existing values are modified by assigning a new value to an existing key.
    ```python
    student_info["age"] = 21
    print(student_info)
    # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grades': {'math': 95, 'physics': 88}, 'city': 'New York'}
    ```

* **Removing Key-Value Pairs:**
    * `del` keyword: Removes a specific key-value pair.
        ```python
        del student_info["city"]
        print(student_info)
        # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'grades': {'math': 95, 'physics': 88}}
        ```
    * `pop(key)` method: Removes the key-value pair and returns the value. Raises `KeyError` if the key is not found,
      unless a default value is provided.
        ```python
        major_removed = student_info.pop("major")
        print(major_removed) # Output: Computer Science
        print(student_info)
        # Output: {'name': 'Alice', 'age': 21, 'grades': {'math': 95, 'physics': 88}}

        # Using pop with a default value to avoid KeyError
        phone = student_info.pop("phone", "N/A")
        print(phone) # Output: N/A
        ```

### 2. Dictionary Methods

Dictionaries provide several useful methods for interacting with their keys, values, and items.

#### Common Dictionary Methods like `keys()`, `values()`, `items()`, and `get()`

* `keys()`: Returns a *view object* that displays a list of all the keys in the dictionary. This view reflects any
  changes made to the dictionary.

    ```python
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(my_dict.keys()) # Output: dict_keys(['a', 'b', 'c'])
    for key in my_dict.keys():
        print(key)
    ```

* `values()`: Returns a *view object* that displays a list of all the values in the dictionary.

    ```python
    print(my_dict.values()) # Output: dict_values([1, 2, 3])
    for value in my_dict.values():
        print(value)
    ```

* `items()`: Returns a *view object* that displays a list of a dictionary's key-value tuple pairs.

    ```python
    print(my_dict.items()) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
    ```

* `get(key, default)`: Returns the value for the specified `key` if the key is in the dictionary. If the key is not
  found, it returns `None` by default, or the `default` value if provided. This is a safer way to access values than
  `[]` as it doesn't raise a `KeyError`.

    ```python
    person = {"name": "Charlie", "age": 25}
    print(person.get("name"))     # Output: Charlie
    print(person.get("city"))     # Output: None
    print(person.get("city", "Unknown")) # Output: Unknown
    ```

Other useful dictionary methods include `clear()`, `copy()`, `update()`, and `popitem()`.

### 3. Sets

Sets are unordered collections of *unique* elements. They are mutable, but their elements must be immutable (like
dictionary keys). Sets are primarily used for membership testing and eliminating duplicate entries from sequences.

#### Creating and Using Sets

Sets are created using curly braces `{}` or the `set()` constructor. Note that an empty set must be created with
`set()`, not `{}` (as `{}` creates an empty dictionary).

**Creating a set:**

```python
# Empty set
empty_set = set()
print(empty_set)  # Output: set()

# Set with initial elements (duplicates are automatically removed)
numbers = {1, 2, 3, 2, 4, 1}
print(numbers)  # Output: {1, 2, 3, 4} (order is not guaranteed)

# Creating a set from a list
my_list = [10, 20, 30, 20, 40]
set_from_list = set(my_list)
print(set_from_list)  # Output: {40, 10, 20, 30}
```

#### Set Operations like Union, Intersection, and Difference

Sets provide efficient methods for performing standard mathematical set operations.

* **Union (`|` or `union()`):** Returns a new set containing all unique elements from both sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1 | set2
    print(union_set)       # Output: {1, 2, 3, 4, 5}
    print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}
    ```

* **Intersection (`&` or `intersection()`):** Returns a new set containing only the elements common to both sets.

    ```python
    intersection_set = set1 & set2
    print(intersection_set)       # Output: {3}
    print(set1.intersection(set2)) # Output: {3}
    ```

* **Difference (`-` or `difference()`):** Returns a new set containing elements that are in the first set but not in the
  second.

    ```python
    difference_set = set1 - set2
    print(difference_set)       # Output: {1, 2}
    print(set1.difference(set2)) # Output: {1, 2}
    ```

* **Symmetric Difference (`^` or `symmetric_difference()`):** Returns a new set containing elements that are in either
  of the sets, but not in both.

    ```python
    symmetric_difference_set = set1 ^ set2
    print(symmetric_difference_set)       # Output: {1, 2, 4, 5}
    print(set1.symmetric_difference(set2)) # Output: {1, 2, 4, 5}
    ```

### 4. Working with Sets

#### Iterating Over Sets and Using Set Methods

You can iterate over the elements of a set using a `for` loop, although the order is not guaranteed.

```python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```

**Common Set Methods:**

* `add(element)`: Adds an element to the set. If the element is already present, nothing happens.
    ```python
    my_set = {1, 2}
    my_set.add(3)
    my_set.add(2) # No effect as 2 is already there
    print(my_set) # Output: {1, 2, 3}
    ```

* `remove(element)`: Removes an element from the set. Raises a `KeyError` if the element is not found.
    ```python
    my_set.remove(3)
    print(my_set) # Output: {1, 2}
    # my_set.remove(5) # This would raise a KeyError
    ```

* `discard(element)`: Removes an element from the set if it is present. Does *not* raise an error if the element is not
  found.
    ```python
    my_set.discard(2)
    my_set.discard(5) # No error
    print(my_set) # Output: {1}
    ```

* `pop()`: Removes and returns an arbitrary element from the set. Raises `KeyError` if the set is empty. Since sets are
  unordered, you cannot predict which element will be removed.

    ```python
    colors = {"red", "green", "blue"}
    popped_color = colors.pop()
    print(popped_color) # Output: (e.g.) red
    print(colors)       # Output: (e.g.) {'green', 'blue'}
    ```

* `clear()`: Removes all elements from the set, making it empty.
    ```python
    colors.clear()
    print(colors) # Output: set()
    ```

Sets are incredibly useful for tasks like efficiently checking for duplicates, performing unique operations, and
optimizing membership tests where the order of elements isn't important.