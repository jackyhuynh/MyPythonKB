# Review Questions for Chapters 5 and 6
## This document contains review questions and answers for Chapters 5 and 6, covering topics such as functions, error handling,

**Functions and Program Structure:**

1. Explain the purpose of a function in programming.(Block of code that performs a specific task)
   Functions allow you to encapsulate code into reusable blocks, making programs more organized and modular.
2. How do you define a function in Python that accepts arguments?
    You define a function using the `def` keyword, followed by the function name and parentheses containing any parameters.
    For example:
    ```python
    def my_function(param1, param2):
         # Function body
        pass
    ```
3. What is the "scope" of a local variable? 
   The scope of a local variable refers to the region of the program where the variable is accessible. 
   Local variables are defined within a function and can only be accessed within that function. They are not visible outside of it, which helps prevent naming conflicts and keeps the code organized.
4. Describe the "top-down" design technique in the context of functions: technique can be used to break down an algorithm into functions.
5. What is a "value-returning function"? 
   A value-returning function is a function that performs a task and then returns a value to the caller using the `return` statement. 
   This allows the function to output a result that can be used later in the program.
6. What is the first line in a function definition called? (header)
7. What is a "block" in the context of a function definition? (A block is a group of statements that are executed together as part of the function. )
   In Python, blocks are defined by indentation, and they contain the code that runs when the function is called.)
8. When a function is called by its name, what happens? (The program control jumps to the function definition, executes the code within the function, and then returns to the point where the function was called.)
9. Explain what an "argument" is when passed into a function.
10. What type of variable is created inside a function? (Local variable)
    A local variable is created inside a function and can only be accessed within that function. It is not visible outside of the function, which helps to avoid naming conflicts with variables in other parts of the program.
11. How does Python handle the `import` statement for modules like `random`? 
    When you use the `import` statement, Python searches for the specified module in its standard library and any directories listed in the `sys.path` variable. If found, it loads the module, making its functions and variables available for use in your program.
12. Provide an example of a Python function that takes two integer arguments and returns the lesser of the two, or zero
    if they are equal.
```python
def find_minimum(val1, val2):
    if val1 < val2:
        return val1
    elif val2 < val1:
        return val2
    else:
        return 0
```

**Error Handling:**

1. What Python statement is used to handle runtime errors? 
   The `try` and `except` statements are used to handle runtime errors in Python. You place the code that might raise an exception inside a `try` block, and you handle the exception in the corresponding `except` block.
   
Example:
```python
def risky_operation():
    # This function might raise an exception
    pass


try:
   # Code that may raise an exception
   risky_operation()
except Exception as e:
   # Handle the exception
   print(f"An error occurred: {e}")
```
2. Explain what happens if a `ZeroDivisionError` occurs in a `try-except` block.
    If a `ZeroDivisionError` occurs in a `try` block, the program control jumps to the corresponding `except` block that handles that specific exception type. The code in the `except` block is executed, allowing you to handle the error gracefully without crashing the program.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
3. What is the purpose of a `ValueError` exception?
    A `ValueError` exception is raised when a function receives an argument of the right type but an inappropriate value. For example, trying to convert a non-numeric string to an integer will raise a `ValueError`.


**File I/O:**

1. List and describe the three essential steps for a program to use a file.(Open, Read/Write, Close)
   - **Open**: The program must open the file using a specific mode (e.g., read, write, append) to access its contents.
   - **Read/Write**: The program can then read from or write to the file as needed.
   - **Close**: Finally, the program must close the file to free up system resources and ensure that all data is saved properly.
2. Which file mode specifier will erase existing file contents and create a new file if it doesn't exist?
3. If a file does not exist and you attempt to open it in append mode, what is the result?
   If you attempt to open a file in append mode (`'a'`) and the file does not exist, Python will create a new file with that name. The file will be opened for appending, meaning you can write data to the end of the file without erasing any existing content.
4. Given a file object `customer_info`, how would you write the string 'Mary Smith' to the file, assuming it was opened
   in write mode?
```python
customer_info = open('customer_info.txt', 'w')
customer_info.write('Mary Smith')
```
5. When data is written to a file, where is it copied from? (The program's memory)
   When data is written to a file, it is copied from the program's memory (specifically, from the variables or data structures in the program) to the file on disk.
6. What is a "file object" and its role in programming? (A file object is an instance of a file that allows you to perform operations like reading, writing, and closing the file. It acts as a bridge between your program and the file system, enabling you to manipulate files easily.)
7. What is a single piece of data within a record called? (A field)
   A single piece of data within a record is called a field. Fields are the individual components that make up a record in a file or database, such as a name, address, or phone number.
8. What is another name for a random access file?(A random access file is also known as a "binary file." It allows for reading and writing data at any position within the file, rather than sequentially from the beginning to the end.)

**Output Prediction and Code Analysis:**

1. Given the following code, what will be the output?
```python
def create_string(first, last):
   combined = str(first) + "_" + str(last)
   return combined

val_a = 10
val_b = 25
result_string = create_string(val_a, val_b)
print(result_string)
```
2. What will be the output of the following code if the user enters 75 and -5 at the prompts?
```python
def analyze_input():
    try:
        total_cost = int(input("Enter total cost of items? "))
        number_of_items = int(input("Number of items "))
        avg_cost = total_cost / number_of_items
    except ZeroDivisionError:
        print('ERROR: cannot have 0 items')
    except ValueError:
        print('ERROR: number of items cannot be negative')
analyze_input()
```
3. What will be the output after the following code is executed?
```python
def calculate_power(base, exponent):
    output = base ** exponent
    return output

base_val = 2
exp_val = 5
final_answer = calculate_power(base_val, exp_val)
print(final_answer)
```
4. What will be the output of the following code if the user enters 75 and 0 at the prompts?
```python
def process_data():
    try:
        cost = int(input("Enter total cost of items? "))
        items_count = int(input("Number of items "))
        avg_per_item = cost / items_count
    except ZeroDivisionError:
        print('ERROR: cannot have 0 items')
    except ValueError:
        print('ERROR: number of items cannot be negative')
process_data()
```
5. What will the following program display?
```python
def program_start():
    value1 = 10
    value2 = 3.5
    print(value1, value2)
    modify_values(value1, value2)
    print(value1, value2)

    
def modify_values(p1, p2):
    p1 = 1
    p2 = 1.0
    print(p1, p2)

    
program_start()
```
6. What will the following code display:
```python
try:
    a = 5
    b = 0
    c = a / b
except FileNotFoundError:
    print('File not found error!')
except ZeroDivisionError:
    print('Division by zero occurred.')
except:
    print('An unexpected error happened.')
```

**General Programming Concepts:**

1. How would you write a loop in Python that displays 5 random numbers in the range of 1 through 100 (inclusive)?
```python
import random

for i in range(5):
    print(random.randrange(1, 101))
```
2. Write Python code that opens an output file named "numbers\_output.txt", writes numbers 1 through 50 to it (each on a
   new line), and then closes the file.
```python
output_file = open('numbers_output.txt', 'w')
for num in range(1, 51):
    output_file.write(str(num) + '\n')
output_file.close()
```
3. What does the statement `first_val, second_val = retrieve_nums()` imply about the `retrieve_nums()` function?
4. Which function returns the largest integer that is less than or equal to its argument? (`math.floor()`)
   The `math.floor()` function returns the largest integer that is less than or equal to its argument. It is part of the `math` module in Python and is used for rounding down floating-point numbers to the nearest whole number.
5. What are "library functions" in Python? (Library functions are pre-defined functions provided by Python's standard library or external libraries that perform common tasks, such as mathematical operations, string manipulation, and file handling. They can be used to simplify coding and avoid reinventing the wheel.)