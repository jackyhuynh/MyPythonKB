## Chapter 5: Functions

As your programs grow more complex, you'll find yourself writing lines of code that perform similar tasks repeatedly.
Copying and pasting code is not only tedious but also makes your programs harder to manage and update. This is where *
*functions** come in. Functions are one of the most fundamental and powerful concepts in programming, allowing you to
organize your code, make it reusable, and simplify complex tasks.

### 1\. Introduction to Functions

A **function** is a block of organized, reusable code that is used to perform a single, related action. Think of a
function as a mini-program within your larger program.

**Benefits of using functions:**

* **Modularity**: Functions break down complex problems into smaller, manageable pieces, making the program easier to
  understand, design, and debug.
* **Reusability**: Once you write a function, you can call it multiple times from different parts of your program or
  even in other programs, avoiding redundant code.
* **Maintainability**: If you need to change how a specific task is performed, you only have to modify the code in one
  place (the function definition), rather than searching for and updating every instance of that code.
* **Readability**: Well-named functions make your code easier to read and understand, as they describe the purpose of a
  block of code.

**Writing and calling functions:**

In Python, you define a function using the `def` keyword, followed by the function name, parentheses `()`, and a colon
`:`. The code block that makes up the function is indented.

```python
# Defining a simple function
def greet_user():
    print("Hello, welcome to the program!")
    print("This is inside the function.")


# Calling the function
greet_user()  # This executes the code inside greet_user()
print("This is outside the function.")
```

When you *call* (or invoke) a function, the program temporarily jumps to the function's code block, executes its
statements, and then returns to the point where the function was called.

### 2\. Void Functions

A **void function** (sometimes called a procedure in other languages) is a function that performs a task but does not
explicitly return a value. While it doesn't return anything, it often produces a side effect, such as printing output to
the console, writing to a file, or modifying an object.

* **Creating and using void functions**: We've already seen an example with `greet_user()`. Here's another:

```python
def display_menu():
  print("--- Main Menu ---")
  print("1. Start Game")
  print("2. Options")
  print("3. Exit")
  print("-----------------")

display_menu() # Call the void function
```

* **The `def` keyword and function naming conventions**:

    * The `def` keyword signals the start of a function definition.
    * Python function names should follow the `snake_case` convention (all lowercase, words separated by underscores),
      as discussed in Chapter 1. They should be descriptive of the action the function performs.

### 3\. Value-Returning Functions

A **value-returning function** is a function that processes some data and then sends a result back to the part of the
program that called it. This result is known as the **return value**.

* **Creating functions that return a value**: You use the `return` statement to send a value back from a function. When
  the `return` statement is executed, the function immediately terminates, and the value specified after `return` is
  sent back.

```python
def add_numbers(num1, num2):
  result = num1 + num2
  return result # Return the calculated sum

# Calling the function and storing its return value
sum_value = add_numbers(10, 5)
print("The sum is:", sum_value) # Output: The sum is: 15

# You can also use the return value directly
print("Another sum:", add_numbers(20, 30)) # Output: Another sum: 50
```

A function can return any Python object, including numbers, strings, lists, or even other functions.

### 4\. Passing Arguments to Functions

Functions often need specific pieces of information to perform their tasks. These pieces of information are called *
*arguments** when passed during a function call, and **parameters** when received in the function definition.

```python
# Function definition with parameters
def introduce(name, age):
    print(f"Hi, my name is {name} and I am {age} years old.")


# Calling the function with arguments

# Positional Arguments: The order matters
introduce("Alice", 30)
introduce(25, "Bob")  # This would be incorrect due to positional mismatch!

# Keyword Arguments: Specify argument by parameter name, order doesn't matter
introduce(age=25, name="Bob")
introduce(name="Charlie", age=35)
```

* **Positional arguments**: Arguments are matched to parameters based on their position in the function call.

* **Keyword arguments**: Arguments are matched to parameters by their name, allowing you to pass them in any order. This
  improves readability for functions with many parameters.

* **The concept of parameter passing and scope**:

    * When you pass arguments to a function, Python usually uses "pass by object reference." For immutable objects (like
      numbers, strings, tuples), changes to the parameter inside the function do *not* affect the original argument
      outside the function. For mutable objects (like lists, dictionaries), changes *can* affect the original object.
    * **Scope**: Variables defined *inside* a function (including its parameters) are **local** to that function. They
      only exist while the function is executing and cannot be accessed from outside the function. This prevents naming
      conflicts and promotes modularity.

  <!-- end list -->

```python
def my_function():
  local_var = 10
  print(local_var)

my_function()
# print(local_var) # This would cause an error because local_var is not defined outside the function
```

### 5\. Global Variables and Constants

While local variables are preferred, sometimes you might encounter or need to use **global variables** and **constants
**.

* **Global Variables**: A variable defined outside of all functions is a global variable. It can be accessed (read) by
  any function in the program. However, modifying a global variable inside a function requires the `global` keyword.
  This is generally discouraged because it makes code harder to debug and understand due to non-local side effects.

```python
global_message = "Hello from global!"

def read_global():
  print(global_message) # Can read global_message

def modify_global():
  # global_message = "New global message" # This would create a new LOCAL variable!
  global global_message # Declare intent to modify the global variable
  global_message = "Modified global message inside function."

read_global()       # Output: Hello from global!
modify_global()
print(global_message) # Output: Modified global message inside function.
```

* **Constants**: In Python, constants are typically global variables whose names are written in
  `ALL_CAPS_WITH_UNDERSCORES` (e.g., `MAX_RETRIES = 5`). By convention, once defined, their values are not changed.
  While Python doesn't strictly enforce immutability for constants, this naming convention signals their intended use.

```python
PI = 3.14159
TAX_RATE = 0.07

def calculate_circle_area(radius):
  return PI * (radius ** 2)

area = calculate_circle_area(5)
print(f"Area: {area}")
```

* **Understanding the implications of using global variables**: Over-reliance on global variables can lead to "spaghetti
  code" where data flow is unclear and functions have hidden dependencies. It makes debugging more difficult and reduces
  code reusability. It's generally best practice to pass data to functions via arguments and receive results via return
  values.

### 6\. Modularizing Programs

**Modularizing programs** means breaking down a large, complex program into smaller, self-contained, and independent
modules or functions. This is arguably one of the most important aspects of good software engineering.

* **Breaking down programs into smaller, manageable functions**:

    * Each function should have a single, well-defined responsibility (the "Single Responsibility Principle").
    * Functions should be relatively short and focused.
    * This makes each part easier to test, debug, and understand.

* **The importance of modular design in programming**:

    * **Simpler Development**: Tackle one small problem at a time.
    * **Easier Debugging**: When an error occurs, you can narrow down the search to a specific function rather than
      sifting through thousands of lines of code.
    * **Code Reusability**: Functions can be easily reused in different parts of the same program or in entirely
      different projects.
    * **Collaboration**: Multiple developers can work on different functions simultaneously without stepping on each
      other's toes.
    * **Scalability**: Well-modularized code is easier to extend and adapt to new requirements.