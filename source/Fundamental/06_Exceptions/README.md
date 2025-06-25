## Chapter 6: Files and Exceptions

So far, our programs have primarily interacted with the user through the console (input and output). However, real-world
applications often need to persist data beyond the program's execution or handle situations where things go wrong. This
chapter introduces you to two crucial concepts: how to work with files for data storage, and how to gracefully handle
errors that might occur during program execution.

### 1\. File Input and Output

Programs can interact with files stored on your computer's disk. This allows them to read existing data (input) or save
new data (output).

The basic workflow for file operations involves three steps:

1. **Opening the file**: You must `open()` a file before you can read from or write to it. When opening, you specify the
   file's path and the mode of operation (read, write, append, etc.).
2. **Performing operations**: Once opened, you can use methods like `read()` to get data from it or `write()` to put
   data into it.
3. **Closing the file**: After you're done with the file, it's crucial to `close()` it. This releases the file lock,
   frees up system resources, and ensures that all buffered data is actually written to the disk.

**Using `open()`, `read()`, `write()`, and `close()` functions:**

* **`open(filename, mode)`**:
    * `filename`: The path to the file you want to open (e.g., `"data.txt"`).
    * `mode`: A string indicating how the file is to be opened:
        * `"r"`: Read mode (default). Error if file doesn't exist.
        * `"w"`: Write mode. Creates a new file or overwrites an existing one.
        * `"a"`: Append mode. Creates a new file or adds to the end of an existing one.
        * `"x"`: Exclusive creation mode. Creates a new file, but errors if the file already exists.
        * `"b"`: Binary mode (e.g., `"rb"`, `"wb"`). For non-text files like images or executables.
        * `"t"`: Text mode (default). For text files.
    * The `open()` function returns a **file object** which you'll use for operations.

<!-- end list -->

```python
# Writing to a file (will overwrite if exists, create if not)
file_path = "my_data.txt"
file_object = open(file_path, "w")
file_object.write("Hello, file world!\n")
file_object.write("This is the second line.\n")
file_object.close()  # CRUCIAL to close the file!

# Reading from a file
file_object = open(file_path, "r")
content = file_object.read()  # Reads entire content as a single string
print("File Content:")
print(content)
file_object.close()

# Appending to a file
file_object = open(file_path, "a")
file_object.write("This line was appended.\n")
file_object.close()

file_object = open(file_path, "r")
print("\nUpdated File Content:")
print(file_object.read())
file_object.close()
```

### 2\. Working with Files

Efficiently managing files often involves more than just reading and writing.

* **Handling file paths and directories**:

    * Files can be in the same directory as your script (relative path) or in a different location (absolute path).
    * Always use platform-independent ways to construct paths, especially for complex applications. The `os.path`
      module (part of Python's standard library `os`) is very useful for this.
    * `os.path.join()`: Safely joins path components.
    * `os.path.exists()`: Checks if a file or directory exists.
    * `os.mkdir()`: Creates a directory.
    * `os.remove()`: Deletes a file.
    * `os.rename()`: Renames a file.

  <!-- end list -->

```python
import os

folder_name = "my_documents"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created directory: {folder_name}")

new_file_path = os.path.join(folder_name, "report.txt")
with open(new_file_path, "w") as f:
    f.write("This is a report in a new folder.")
print(f"File created at: {new_file_path}")
```

* **Using loops to process files**: For text files, you often want to process them line by line. File objects are
  iterable, making `for` loops ideal for this.

```python
print("\nReading file line by line:")
with open("my_data.txt", "r") as f:  # Using 'with' statement for auto-closing
    for line in f:
        print(f"Line: {line.strip()}")  # .strip() removes leading/trailing whitespace like newline chars
```

The `with open(...) as ...:` statement is the preferred way to handle files in Python. It ensures that the file is
automatically closed, even if errors occur, preventing resource leaks.

### 3\. Exceptions

An **exception** is an event that occurs during the execution of a program that disrupts the normal flow of
instructions. When an error occurs that Python cannot handle, it raises an exception. If not handled, this leads to a
program crash.

* **Introduction to exception handling**: Exception handling allows your program to gracefully deal with errors,
  preventing crashes and providing a better user experience.

* **Using `try`, `except`, `else`, and `finally` blocks**:

    * **`try`**: The block of code that might raise an exception. You put the risky code here.
    * **`except`**: The block of code that executes if a specific type of exception occurs in the `try` block. You can
      have multiple `except` blocks for different exception types.
    * **`else`**: (Optional) The block of code that executes if the `try` block completes successfully without raising
      any exception.
    * **`finally`**: (Optional) The block of code that *always* executes, regardless of whether an exception occurred or
      not. It's often used for cleanup operations (like closing files or releasing resources).

  <!-- end list -->

```python
try:
    num1_str = input("Enter a number: ")
    num2_str = input("Enter another number: ")
    num1 = int(num1_str)
    num2 = int(num2_str)
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:  # Catch any other unexpected exception
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The division result is: {result}")
finally:
    print("Calculation attempt finished.")  # This always runs
```

### 4\. Exception Object

When an exception occurs, Python creates an **exception object** that contains information about the error. You can
catch this object to inspect details about the problem.

* **Working with exception objects to get more information about errors**: You can use
  `except ExceptionType as variable_name:` to capture the exception object. The `variable_name` will hold the exception
  instance, which you can then print or use to log details.

  ```python
  try:
      my_list = [1, 2, 3]
      print(my_list[5]) # This will raise an IndexError
  except IndexError as e:
      print(f"Caught an IndexError: {e}") # e will contain details like "list index out of range"
  ```

* **Raising exceptions manually**: Sometimes, your own code might detect a situation that is an error, and you want to
  explicitly stop execution and signal that error. You can do this using the `raise` statement.

```python
def process_positive_number(num):
    if num < 0:
        raise ValueError("Input number must be positive!")
    print(f"Processing number: {num}")


try:
    process_positive_number(-5)
except ValueError as e:
    print(f"Error: {e}")

process_positive_number(10)
```