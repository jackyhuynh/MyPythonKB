## Chapter 15: Advanced Sorting and Searching

This chapter delves into more sophisticated sorting and searching algorithms. While Python's built-in `sort()` and
`sorted()` functions are highly optimized, understanding these advanced algorithms provides critical insights into
algorithmic efficiency and problem-solving techniques.

### 1. Sorting Algorithms

Sorting is the process of arranging elements in a list or array in a specific order (e.g., ascending or descending).

#### Understanding and Implementing Advanced Sorting Algorithms like Quicksort and Mergesort

* **Quicksort:**
  Quicksort is a highly efficient, comparison-based sorting algorithm that uses a **divide-and-conquer** strategy.
    1. **Divide:** Pick an element from the array, called a **pivot**.
    2. **Conquer (Partition):** Rearrange the array such that all elements less than the pivot come before it, and all
       elements greater than the pivot come after it. The pivot is now in its final sorted position.
    3. **Combine (Recurse):** Recursively apply the above steps to the sub-arrays of elements with smaller values and
       separately to the sub-arrays of elements with greater values.

    * **Time Complexity:**
        * Average Case: $O(N \log N)$
        * Worst Case: $O(N^2)$ (occurs when the pivot selection consistently leads to highly unbalanced partitions,
          e.g., already sorted array and always picking first/last element as pivot).
    * **Space Complexity:** $O(\log N)$ on average (due to recursion stack), $O(N)$ in worst case.
    * **In-place:** Yes, it sorts the array without requiring significant extra space.

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] # Choose middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage
data_quick = [3, 6, 8, 10, 1, 2, 1]
print("Original (Quick):", data_quick)
sorted_data_quick = quicksort(data_quick)
print("Sorted (Quick):", sorted_data_quick) # Output: [1, 1, 2, 3, 6, 8, 10]
```

* **Mergesort:**
  Mergesort is another comparison-based sorting algorithm that also follows the **divide-and-conquer** paradigm.
    1. **Divide:** Recursively divide the unsorted list into $N$ sublists, each containing one element (a list of one
       element is considered sorted).
    2. **Conquer (Merge):** Repeatedly merge sublists to produce new sorted sublists until there is only one sorted list
       remaining.

    * **Time Complexity:** $O(N \log N)$ in all cases (best, average, worst). This makes it more stable than Quicksort
      in terms of performance.
    * **Space Complexity:** $O(N)$ (requires auxiliary space for merging).
    * **Stable:** Yes, it preserves the relative order of equal elements.

```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergesort(left_half)
    right_half = mergesort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

# Example usage
data_merge = [38, 27, 43, 3, 9, 82, 10]
print("Original (Merge):", data_merge)
sorted_data_merge = mergesort(data_merge)
print("Sorted (Merge):", sorted_data_merge) # Output: [3, 9, 10, 27, 38, 43, 82]
```

### 2. Searching Algorithms

Searching is the process of finding a specific item within a collection of items.

#### Implementing Advanced Searching Algorithms like Binary Search and Hash Tables

* **Binary Search:**
  Binary search is an efficient algorithm for finding an item from a *sorted* list of items. It repeatedly divides the
  search interval in half.
    1. Compare the target value with the middle element of the list.
    2. If they are equal, the position is found.
    3. If the target is smaller, search the left half.
    4. If the target is larger, search the right half.
    5. Repeat until the target is found or the interval becomes empty.

    * **Prerequisite:** The list *must* be sorted.
    * **Time Complexity:** $O(\log N)$ (very efficient for large lists).
    * **Space Complexity:** $O(1)$ (iterative) or $O(\log N)$ (recursive due to call stack).

```python
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else: # arr[mid] > target
            high = mid - 1
    return -1 # Not found

# Example usage
sorted_numbers = [5, 10, 15, 20, 25, 30]
print("Index of 20:", binary_search_iterative(sorted_numbers, 20)) # Output: 3
print("Index of 12:", binary_search_iterative(sorted_numbers, 12)) # Output: -1
```

(Recursive version of binary search was covered in Chapter 12: Recursion)

* **Hash Tables (Dictionaries in Python):**
  A hash table (or hash map) is a data structure that implements an associative array abstract data type, mapping keys
  to values. It uses a **hash function** to compute an index into an array of buckets or slots, from which the desired
  value can be found.

  In Python, dictionaries (`dict`) are implemented using hash tables. They provide extremely fast average-case lookup,
  insertion, and deletion operations.

    * **How it works (simplified):**
        1. When you add a key-value pair, the hash function takes the key and converts it into a numerical hash value.
        2. This hash value is then mapped to an index in an underlying array.
        3. The value is stored at that index.
        4. When you look up a key, the same hash function generates the same index, allowing direct access to the value.

        * **Collisions:** Different keys might produce the same hash value (a "collision"). Hash tables have strategies
          to handle collisions (e.g., separate chaining, open addressing).

    * **Time Complexity:**
        * Average Case: $O(1)$ (constant time) for insertion, deletion, and lookup.
        * Worst Case: $O(N)$ (occurs in cases of many collisions, leading to linear search within a bucket).
    * **Space Complexity:** $O(N)$ (to store the elements).

```python
# Python dictionaries are hash tables
student_grades = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-"
}

# Lookup (average O(1))
print(student_grades["Alice"]) # Output: A

# Insertion (average O(1))
student_grades["David"] = "C"
print(student_grades)

# Deletion (average O(1))
del student_grades["Bob"]
print(student_grades)

# Checking membership (average O(1))
print("Charlie" in student_grades) # Output: True
print("Eve" in student_grades)     # Output: False
```

Hash tables are the backbone of many high-performance applications, including databases, caches, and symbol tables in
compilers.

### 3. Efficiency of Algorithms

#### Understanding the Efficiency and Complexity of Algorithms

Algorithm efficiency refers to the computational resources (time and space) an algorithm uses to solve a problem. It's
crucial for choosing the best algorithm, especially for large datasets.

* **Time Complexity:** How the running time of an algorithm grows as the input size (N) grows.
* **Space Complexity:** How the memory usage of an algorithm grows as the input size (N) grows.

We aim for algorithms that perform well, meaning their time and space requirements don't increase too rapidly with
larger inputs.

#### Using Big O Notation to Analyze the Performance of Algorithms

**Big O notation** is a mathematical notation that describes the limiting behavior of a function when the argument tends
towards a particular value or infinity. In computer science, it's used to classify algorithms by how their running time
or space requirements grow as the input size grows. It describes the *upper bound* of the growth rate.

**Common Big O Notations (from best to worst performance for large N):**

* **$O(1)$ - Constant Time:** The execution time or space requirement does not change with the input size.
    * Example: Accessing an element in an array by index, checking if a key exists in a hash table.
* **$O(\log N)$ - Logarithmic Time:** The execution time or space requirement grows logarithmically with the input size.
  This is very efficient; doubling the input size only increases time by a small, constant amount.
    * Example: Binary search.
* **$O(N)$ - Linear Time:** The execution time or space requirement grows directly proportional to the input size.
    * Example: Iterating through a list to find an element, sum of all elements in an array.
* **$O(N \log N)$ - Linearithmic Time:** A very common complexity for efficient sorting algorithms.
    * Example: Mergesort, Quicksort (average case).
* **$O(N^2)$ - Quadratic Time:** The execution time or space requirement grows as the square of the input size. Often
  seen in algorithms with nested loops.
    * Example: Bubble Sort, Selection Sort, Insertion Sort (worst case), comparing every element with every other
      element.
* **$O(2^N)$ - Exponential Time:** The execution time or space requirement doubles with each addition to the input size.
  Very inefficient for even moderately sized inputs.
    * Example: Naive recursive Fibonacci, some brute-force algorithms.
* **$O(N!)$ - Factorial Time:** Extremely inefficient.
    * Example: Traveling Salesperson Problem (brute-force).

**Example of Analysis:**

Consider finding the sum of all elements in a list:

```python
def sum_list(arr):
    total = 0 # O(1)
    for x in arr: # Loop runs N times
        total += x # O(1) operation inside loop
    return total # O(1)
```

The dominant part is the loop that runs `N` times. Thus, the time complexity is $O(N)$.

Understanding Big O notation is fundamental for designing efficient algorithms and making informed decisions about which
data structures and algorithms to use for a given problem. It allows you to predict how an algorithm will scale with
increasing data.