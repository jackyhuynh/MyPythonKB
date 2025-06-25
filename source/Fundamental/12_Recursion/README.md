## Chapter 12: Recursion

This chapter introduces **recursion**, a powerful programming technique where a function calls itself to solve a
problem. It's often used for problems that can be broken down into smaller, self-similar subproblems.

### 1. Introduction to Recursion

#### Understanding the Concept of Recursion

Recursion is a method of solving problems by breaking them down into smaller instances of the same problem until a
simple base case is reached. A recursive function is a function that calls itself, either directly or indirectly.

Think of it like a set of Russian nesting dolls: each doll contains a smaller version of itself, until you reach the
smallest doll which contains nothing else.

#### Writing Recursive Functions

Every recursive function must have two main parts:

1. **Base Case:** The condition that stops the recursion. Without a base case, a recursive function would call itself
   indefinitely, leading to a "stack overflow" error. This is the simplest instance of the problem that can be solved
   directly.
2. **Recursive Case:** The part where the function calls itself with a smaller version of the original problem. This
   step moves the problem closer to the base case.

### 2. How Recursion Works

Let's illustrate with a simple example: calculating the factorial of a number ($n!$).
The factorial of $n$ is $n \times (n-1) \times (n-2) \times \dots \times 1$.
The base case for factorial is $0! = 1$ and $1! = 1$.
The recursive definition is $n! = n \times (n-1)!$ for $n > 1$.

```python
def factorial(n):
    # Base Case: When n is 0 or 1, factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive Case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
print(factorial(0))  # Output: 1
```

**How `factorial(5)` executes:**

1. `factorial(5)` calls `5 * factorial(4)`
2. `factorial(4)` calls `4 * factorial(3)`
3. `factorial(3)` calls `3 * factorial(2)`
4. `factorial(2)` calls `2 * factorial(1)`
5. `factorial(1)` returns `1` (base case)
6. `factorial(2)` receives `1`, returns `2 * 1 = 2`
7. `factorial(3)` receives `2`, returns `3 * 2 = 6`
8. `factorial(4)` receives `6`, returns `4 * 6 = 24`
9. `factorial(5)` receives `24`, returns `5 * 24 = 120`

### 3. Examples of Recursive Algorithms

Recursion is well-suited for problems that exhibit a recursive structure.

* **Factorial (as above)**

* **Fibonacci Sequence:** A sequence where each number is the sum of the two preceding ones, usually starting with 0 and
    1. (0, 1, 1, 2, 3, 5, 8, ...)
       Base cases: `fib(0) = 0`, `fib(1) = 1`
       Recursive case: `fib(n) = fib(n-1) + fib(n-2)`

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))  # Output: 13
```

    *Note: A naive recursive Fibonacci implementation is inefficient due to repeated calculations. Memoization or iteration is generally preferred for this specific problem.*

* **Binary Search (on a sorted list):** Efficiently finds the position of a target value within a sorted list.
    * Base case: If the list is empty or the target is found.
    * Recursive case: Divide the list in half and search the appropriate half.

```python
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1  # Element not present


sorted_list = [2, 3, 4, 10, 40]
result = binary_search(sorted_list, 0, len(sorted_list) - 1, 10)
print(f"Element is present at index {result}")  # Output: Element is present at index 3
```

### 4. Recursion vs. Iteration

#### Comparing Recursion and Iteration

Many problems can be solved using both recursion and iteration (loops).

| Feature            | Recursion                                             | Iteration (Loops)                              |
|:-------------------|:------------------------------------------------------|:-----------------------------------------------|
| **Structure**      | Function calls itself                                 | Uses loops (for, while) to repeat code         |
| **Base Case**      | Essential for termination                             | Loop termination condition                     |
| **Memory**         | Uses more memory (call stack)                         | Generally more memory-efficient                |
| **Complexity**     | Can be elegant for complex problems                   | Often more straightforward for simple problems |
| **Readability**    | Can be more readable for naturally recursive problems | Can be less readable for deeply nested logic   |
| **Performance**    | Can be slower due to function call overhead           | Generally faster for same task                 |
| **Stack Overflow** | Risk of stack overflow for deep recursion             | No stack overflow risk                         |

#### Understanding the Pros and Cons of Using Recursion

**Pros of Recursion:**

* **Elegance and Readability:** For problems that are naturally recursive (like tree traversals, fractal generation),
  recursive solutions can be much cleaner and more intuitive.
* **Reduced Code:** Can often lead to more concise code.

**Cons of Recursion:**

* **Memory Overhead:** Each recursive call adds a new stack frame to the call stack. Deep recursion can lead to
  `RecursionError` (stack overflow).
* **Performance:** Function call overhead can make recursive solutions slower than iterative ones for certain problems.
* **Debugging:** Can be harder to trace and debug due to the multiple function calls.

**When to use recursion:**

* When the problem inherently has a recursive structure (e.g., tree and graph algorithms, certain mathematical
  sequences).
* When a recursive solution is significantly more readable and simpler than an iterative one.
* When the depth of recursion is not expected to be excessively large.

For simple iterative tasks like summing numbers in a list, iteration is almost always the better choice. For complex
problems, the elegance of recursion might outweigh its performance drawbacks, or techniques like **memoization** (
dynamic programming) can be used to optimize recursive solutions.

---
