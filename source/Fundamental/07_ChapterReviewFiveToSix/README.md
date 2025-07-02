# Review Questions for Chapters 5 and 6
## This document contains review questions and answers for Chapters 5 and 6, covering topics such as functions, error handling,

**Functions and Program Structure:**

1. Explain the purpose of a function in programming.
2. How do you define a function in Python that accepts arguments?
3. What is the "scope" of a local variable?
4. Describe the "top-down" design technique in the context of functions.
5. What is a "value-returning function"?
6. What is the first line in a function definition called?
7. What is a "block" in the context of a function definition?
8. When a function is called by its name, what happens?
9. Explain what an "argument" is when passed into a function.
10. What type of variable is created inside a function?
11. How does Python handle the `import` statement for modules like `random`?
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
2. Explain what happens if a `ZeroDivisionError` occurs in a `try-except` block.
3. What is the purpose of a `ValueError` exception?

**File I/O:**

1. List and describe the three essential steps for a program to use a file.
2. Which file mode specifier will erase existing file contents and create a new file if it doesn't exist?
3. If a file does not exist and you attempt to open it in append mode, what is the result?
4. Given a file object `customer_info`, how would you write the string 'Mary Smith' to the file, assuming it was opened
   in write mode?
```python
customer_info = open('customer_info.txt', 'w')
customer_info.write('Mary Smith')
```
5. When data is written to a file, where is it copied from?
6. What is a "file object" and its role in programming?
7. What is a single piece of data within a record called?
8. What is another name for a random access file?

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
4. Which function returns the largest integer that is less than or equal to its argument?
5. What are "library functions" in Python?