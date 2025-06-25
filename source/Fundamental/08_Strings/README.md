## Chapter 8: More About Strings

Strings are fundamental data types in many programming languages, used to represent text. This chapter delves deeper
into the nuances of working with strings, exploring their unique properties, powerful manipulation techniques, and
various formatting options.

### 1. String Basics

At its core, a string is a sequence of characters. In many programming languages, strings are enclosed in single
quotes (`'...'`), double quotes (`"..."`), or even triple quotes (`'''...'''` or `"""..."""`) for multi-line strings.

#### Understanding Strings and Their Immutability

A crucial concept to grasp about strings is their **immutability**. This means that once a string is created, its
content cannot be changed. Any operation that appears to modify a string, such as concatenation or replacement, actually
results in the creation of a *new* string in memory. The original string remains untouched.

**Example:**

```python
my_string = "hello"
print(id(my_string))  # Print memory address of the string

my_string = my_string + " world"  # This creates a NEW string
print(id(my_string))  # The memory address will be different
```

Understanding immutability is important for optimizing performance and avoiding unexpected behavior, especially when
dealing with large strings or frequent modifications.

#### Common String Operations and Methods

Despite their immutability, strings offer a rich set of operations and built-in methods for manipulation and inspection.

**Common Operations:**

* **Concatenation:** Joining strings together using the `+` operator.

```python
greeting = "Hello"
name = "Alice"
full_message = greeting + ", " + name + "!"
print(full_message) # Output: Hello, Alice!
```

* **Repetition:** Repeating a string multiple times using the `*` operator.

```python
separator = "-" * 10
print(separator) # Output: ----------
```

* **Length:** Getting the number of characters in a string using the `len()` function.

```python
text = "Python"
length = len(text)
print(length) # Output: 6
```

* **Membership (in/not in):** Checking if a substring exists within a string.

```python
sentence = "The quick brown fox"
print("quick" in sentence)    # Output: True
print("lazy" not in sentence) # Output: True
```

### 2. String Slicing and Indexing

Strings are ordered sequences, which means each character has a specific position, or **index**. This allows you to
access individual characters or extract portions of a string using **indexing** and **slicing**.

#### Accessing Characters and Substrings Using Indexing and Slicing

* **Indexing:** Individual characters are accessed using square brackets `[]` and their index. Indices start from `0`
  for the first character. Negative indices can be used to access characters from the end of the string, with `-1` being
  the last character.

```python
word = "Example"
print(word[0])  # Output: E (first character)
print(word[3])  # Output: m (fourth character)
print(word[-1]) # Output: e (last character)
print(word[-7]) # Output: E (first character, using negative index)
```

* **Slicing:** To extract a portion (substring) of a string, you use slicing with the format `[start:end:step]`.

    * `start`: The starting index (inclusive). If omitted, defaults to `0`.
    * `end`: The ending index (exclusive). If omitted, defaults to the end of the string.
    * `step`: The increment between characters (optional, defaults to `1`).

```python
message = "Programming"

print(message[0:3])   # Output: Pro (characters from index 0 up to (but not including) 3)
print(message[4:])    # Output: ramming (characters from index 4 to the end)
print(message[:5])    # Output: Progr (characters from the beginning up to (but not including) 5)
print(message[:])     # Output: Programming (a copy of the entire string)
print(message[::2])   # Output: Pogamn (every second character)
print(message[::-1])  # Output: gnimmargoP (reversed string)
```

### 3. String Methods

Strings come equipped with a rich set of built-in methods that provide powerful functionalities for manipulating,
searching, and transforming text.

#### Using String Methods like `find()`, `replace()`, `split()`, and `join()`

* `find(substring, start, end)`: Returns the lowest index in the string where `substring` is found. Returns `-1` if not
  found. Optional `start` and `end` arguments specify the search range.

```python
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.find("fox"))      # Output: 16
print(sentence.find("cat"))      # Output: -1
print(sentence.find("the", 20))  # Output: 31 (finds 'the' after index 20)
```

* `replace(old, new, count)`: Returns a new string with all occurrences of `old` replaced by `new`. The optional `count`
  argument specifies the maximum number of replacements.

```python
text = "Hello world, hello Python!"
new_text = text.replace("hello", "hi")
print(new_text) # Output: Hi world, hi Python!

another_text = text.replace("hello", "hi", 1)
print(another_text) # Output: Hi world, hello Python!
```

* `split(separator)`: Splits the string into a list of substrings based on the `separator`. If `separator` is not
  specified, it splits by whitespace.

```python
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits) # Output: ['apple', 'banana', 'cherry']

sentence = "This is a sample sentence."
words = sentence.split()
print(words) # Output: ['This', 'is', 'a', 'sample', 'sentence.']
```

* `join(iterable)`: Concatenates the elements of an iterable (e.g., a list of strings) into a single string, using the
  string on which the method is called as a separator.

```python
words = ["Python", "is", "awesome"]
joined_string = " ".join(words)
print(joined_string) # Output: Python is awesome

path_elements = ["usr", "local", "bin"]
full_path = "/".join(path_elements)
print(full_path) # Output: usr/local/bin
```

Other useful string methods include `lower()`, `upper()`, `capitalize()`, `title()`, `strip()`, `lstrip()`, `rstrip()`,
`startswith()`, `endswith()`, `isdigit()`, `isalpha()`, and many more. Familiarize yourself with the documentation for a
comprehensive list.

### 4. String Formatting

String formatting is essential for creating well-structured and readable output. It allows you to embed values into
strings in a controlled manner.

#### Formatting Strings Using Various Techniques

Historically, several methods have been used for string formatting.

* **Old-style `%` formatting (printf-style):** Similar to C's `printf()`, this uses the `%` operator with format
  specifiers. While still functional, it's generally less preferred in modern Python for new code due to its less
  readable syntax.

```python
name = "Bob"
age = 30
print("My name is %s, and I am %d years old." % (name, age))
# Output: My name is Bob, and I am 30 years old.
```

#### Using Formatted String Literals (f-strings) and the `format()` Method

* **`format()` method:** Introduced in Python 2.6, the `format()` method provides a more flexible and readable way to
  format strings. It uses curly braces `{}` as placeholders.

```python
item = "laptop"
price = 1200.50
quantity = 2

message = "You purchased {} {} for ${:.2f} each. Total: ${:.2f}".format(quantity, item, price, quantity * price)
print(message)
# Output: You purchased 2 laptop for $1200.50 each. Total: $2401.00
```

The `:.2f` inside the placeholder is a format specifier, indicating a floating-point number with two decimal places.

* **Formatted String Literals (f-strings):** Introduced in Python 3.6, f-strings are the most recommended and convenient
  way to format strings. They are prefixed with an `f` (or `F`) and allow you to embed expressions directly inside curly
  braces `{}` within the string.

```python
item = "monitor"
price = 350.75
quantity = 3

# Direct embedding of variables and expressions
message = f"You purchased {quantity} {item} for ${price:.2f} each. Total: ${quantity * price:.2f}"
print(message)
# Output: You purchased 3 monitor for $350.75 each. Total: $1052.25

# You can also include function calls or more complex expressions
import datetime
current_time = datetime.datetime.now()
print(f"Current time: {current_time:%Y-%m-%d %H:%M:%S}")
# Output: Current time: 2025-05-25 14:52:25 (approximately, depends on current time)
```

F-strings offer excellent readability and conciseness, making them the preferred choice for string formatting in modern
Python. They also support various format specifiers (e.g., for alignment, padding, number formatting) for fine-grained
control over the output.
