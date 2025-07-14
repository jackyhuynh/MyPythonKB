## Mostly Use Syntax for Problem-Solving

### I. Data Structures & Collections

#### A. Lists

* **List Comprehensions:** Concise way to create lists.
    * Basic: `[expression for item in iterable]`
    * With `if`: `[expression for item in iterable if condition]`
    * With `if/else`: `[expr_if_true if condition else expr_if_false for item in iterable]`
* **List Slicing:** Extract sub-lists: `my_list[start:end:step]`
    * `my_list[:]` (full copy)
    * `my_list[start:]`
    * `my_list[:end]`
    * `my_list[::2]` (every second item)

#### B. Strings

* **String to List/Dict:**
    * String to list of characters: `list("mystring")` -\> `['m', 'y', 's', 't', 'r', 'i', 'n', 'g']`
    * String splitting: `my_string.split('delimiter')`
    * Creating dict from string (e.g., character counts, see `Counter` below).
* **String Manipulation:** `"".join(list_of_chars)` (joining characters/list elements)
* **Character Case:** `char.isupper()`, `char.islower()`, `char.isalpha()`, `char.isdigit()`, `char.isalnum()`

#### C. Sets

* **Creation:** `my_set = set(my_list)`
* **Operations:**
    * **Union:** `set1 | set2`
    * **Intersection:** `set1 & set2` (Note: your original note had `set1 + set2`, which is incorrect for sets)
    * **Difference:** `set1 - set2` (elements in set1 but not set2)
    * **Symmetric Difference:** `set1 ^ set2` (elements in either set but not in both)
    * **Subset:** `set1 <= set2` (True if set1 is a subset of set2)

#### D. Dictionaries

* **Sorting by Value:** `sorted_items = sorted(my_dict.items(), key=lambda item: item[1])`

#### E. `collections` Module

* **`collections.Counter`:** Efficiently count item frequencies (e.g., characters in a string, elements in a list).
    * `from collections import Counter`
    * `char_counts = Counter("hello world")`
    * `element_counts = Counter([1, 2, 2, 3, 1])`

### II. Control Flow & Iteration

* **`enumerate()`:** Get (index, value) pairs while iterating.
    * `for index, item in enumerate(my_list):`
    * Useful for: `for i, row in enumerate(submatrix):`

### III. Type Checking

* **`isinstance()`:** Check if an object is of a specific data type (or a subclass thereof).
    * `isinstance(value, dict)`
    * `isinstance(value, (int, float))` (check against multiple types)

### IV. Algorithms & Techniques

* **Two-Pointer Technique:** Useful for slicing strings/lists or finding similar characteristics.
* **Character Shifting (Caesar Cipher style):**
    * `chr(ord(letter) + shift)`
    * Handle wrapping (e.g., 'z' to 'a') with modulo `%`:
      `next_char = 'a' if letter == 'z' else chr(ord(letter) + 1)` (This specifically for `+1` shift)
      *More general:* `shifted_ascii = ((ord(char) - ord('a') + shift) % 26) + ord('a')`

### V. Time Manipulation

* **Manual Modulo Arithmetic:** For time cycles (e.g., 24-hour clock).
    * `total_seconds = (seconds_since_start + seconds) % (24 * 3600)`
    * `hours, remainder = divmod(total_seconds, 3600)`
    * `minutes, seconds = divmod(remainder, 60)`
* **`datetime` Module (Recommended for Robust Time Handling):**
    * `import datetime`
* Example:
```python
import datetime
time_points = ['01:00:00', '12:30:15']
time_list = [time_str.split(':') for time_str in time_points]
diff_time_list = [
  (datetime.datetime(100,1,1,int(t[0]),int(t[1]),int(t[2])) + datetime.timedelta(0, seconds_to_add))
  .strftime("%H:%M:%S")
  for t in time_list
]
```
  *Note: `datetime.datetime(100,1,1,...)` uses an arbitrary year/month/day to create a time object.*
  *Note: The original example for `diff_time_list` was slightly off. `seconds` should be `seconds_to_add` for
  clarity.*

### VI. Other Concepts

* **Logical Bitwise Operators:** (`&`, `|`, `^`, `~`, `<<`, `>>`) - Learn their use cases for low-level operations,
  flags, or optimizing certain numerical tasks.