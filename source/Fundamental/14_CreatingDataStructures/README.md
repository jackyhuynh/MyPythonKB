## Chapter 14: Creating Your Own Data Structures

This chapter moves beyond Python's built-in data types (lists, dictionaries, sets) and explores how to build your own
custom data structures. Understanding fundamental data structures is crucial for designing efficient algorithms and
solving complex programming problems.

### 1. Introduction to Data Structures

#### Understanding the Importance of Data Structures

A **data structure** is a specialized format for organizing, processing, retrieving, and storing data. The choice of
data structure can significantly impact the efficiency of an algorithm, especially in terms of time and space
complexity. For example, searching for an item in an unsorted list is much slower than searching in a sorted list using
binary search, or in a hash table.

**Why custom data structures?**

* **Efficiency:** Optimize specific operations (e.g., fast insertions, deletions, or lookups) that built-in types might
  not provide optimally for a given problem.
* **Problem-Specific Needs:** Some problems naturally map to certain data structures (e.g., managing tasks in an
  operating system often uses a queue).
* **Understanding Fundamentals:** Learning to build them from scratch deepens your understanding of how data is managed
  and how algorithms work.

#### Creating Custom Data Structures in Python

In Python, you typically implement custom data structures using **classes**. Classes allow you to encapsulate the data (
attributes) and the operations (methods) that act upon that data.

### 2. Stacks and Queues

Stacks and queues are linear data structures that follow specific rules for adding and removing elements. They are
widely used in various applications, from managing function calls to handling print jobs.

#### Implementing Stacks and Queues Using Lists and Classes

* **Stack (LIFO - Last In, First Out):**
  Imagine a stack of plates. You can only add a plate to the top, and you can only remove a plate from the top. The last
  plate added is the first one removed.
    * **`push` operation:** Adds an element to the top of the stack.
    * **`pop` operation:** Removes and returns the top element from the stack.
    * **`peek` (or `top`) operation:** Returns the top element without removing it.
    * **`is_empty` operation:** Checks if the stack is empty.

  **Implementation using Python lists (simple):**
  Python lists provide `append()` (for push) and `pop()` (for pop) which make them suitable for basic stack
  implementations.

```python
stack = ['A', 'B', 'C']
print("Stack:", stack)  # Output: ['A', 'B', 'C']

print("Popped:", stack.pop())  # Output: C
print("Stack:", stack)  # Output: ['A', 'B']
```

    **Implementation using a Class:**

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print("Stack size:", my_stack.size())  # Output: 2
print("Top element:", my_stack.peek())  # Output: 20
print("Popped element:", my_stack.pop())  # Output: 20
print("Stack is empty?", my_stack.is_empty())  # Output: False
```

* **Queue (FIFO - First In, First Out):**
  Imagine a line at a supermarket. The first person in line is the first one to be served.
    * **`enqueue` operation:** Adds an element to the rear (end) of the queue.
    * **`dequeue` operation:** Removes and returns the element from the front (beginning) of the queue.
    * **`peek` (or `front`) operation:** Returns the front element without removing it.
    * **`is_empty` operation:** Checks if the queue is empty.

  **Implementation using Python lists:**
  Using `append()` for enqueue is efficient. However, `pop(0)` for dequeue is inefficient for large lists because it
  requires shifting all subsequent elements. For performance-critical queues, `collections.deque` is preferred.

```python
queue = ['X', 'Y', 'Z']
print("Queue:", queue)  # Output: ['X', 'Y', 'Z']

print("Dequeued:", queue.pop(0))  # Dequeue (inefficient for large lists)
print("Queue:", queue)  # Output: ['Y', 'Z']
```

    **Implementation using `collections.deque` (recommended for queues):**
    `deque` (double-ended queue) is optimized for additions and removals from both ends.

```python
from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()  # Efficient removal from left

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)


my_queue = Queue()
my_queue.enqueue("Task1")
my_queue.enqueue("Task2")
print("Queue size:", my_queue.size())  # Output: 2
print("Front element:", my_queue.front())  # Output: Task1
print("Dequeued element:", my_queue.dequeue())  # Output: Task1
print("Queue is empty?", my_queue.is_empty())  # Output: False
```

### 3. Linked Lists

Unlike arrays/lists which store elements in contiguous memory locations, a **linked list** stores elements
non-contiguously. Each element (called a **node**) contains the data and a reference (or pointer) to the next node in
the sequence.

#### Understanding and Implementing Linked Lists

**Key Concepts:**

* **Node:** The basic building block of a linked list. It typically has two parts: `data` and `next` (a pointer to the
  next node).
* **Head:** A pointer to the first node in the list. If the list is empty, the head is `None`.
* **Traversal:** Visiting each node in the list sequentially.

**Types of Linked Lists:**

* **Singly Linked List:** Each node points only to the next node.
* **Doubly Linked List:** Each node points to both the next and the previous node.
* **Circular Linked List:** The last node points back to the first node.

**Advantages:**

* **Dynamic Size:** Can grow or shrink easily.
* **Efficient Insertions/Deletions:** Adding or removing elements at specific positions (once found) is very fast, as it
  only involves changing a few pointers.

**Disadvantages:**

* **No Random Access:** To access an element, you must traverse from the head. This makes indexing by position (like
  lists) slow.
* **More Memory:** Each node requires extra space for the pointer.

**Implementation of a Singly Linked List:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # Key not found
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()  # Output: 1 -> 2 -> 3

my_list.prepend(0)
my_list.display()  # Output: 0 -> 1 -> 2 -> 3

my_list.delete_node(2)
my_list.display()  # Output: 0 -> 1 -> 3
```

### 4. Binary Trees

A **binary tree** is a hierarchical data structure in which each node has at most two children, referred to as the left
child and the right child.

#### Introduction to Binary Trees and Their Operations

**Key Concepts:**

* **Root:** The topmost node of the tree.
* **Node:** Each element in the tree, containing data and pointers to left and right children (can be `None`).
* **Child/Parent:** A node directly below another is a child; the node directly above is the parent.
* **Leaf Node:** A node with no children.
* **Subtree:** A portion of a tree that is itself a tree.
* **Depth/Height:** The number of edges from the root to a node (depth) or from a node to the deepest leaf (height).

**Types of Binary Trees:**

* **Full Binary Tree:** Every node has either zero or two children.
* **Complete Binary Tree:** All levels are completely filled except possibly the last level, and all nodes in the last
  level are as far left as possible.
* **Perfect Binary Tree:** All internal nodes have two children and all leaves are at the same level.
* **Balanced Binary Tree:** The heights of the left and right subtrees of every node differ by at most 1 (e.g., AVL
  tree, Red-Black tree).
* **Binary Search Tree (BST):** A special type where for every node, all values in its left subtree are less than its
  value, and all values in its right subtree are greater. This allows for efficient searching, insertion, and deletion.

**Common Operations:**

* **Insertion:** Adding a new node to the tree.
* **Deletion:** Removing a node from the tree.
* **Traversal:** Visiting each node in a specific order.
    * **Inorder Traversal (Left -> Root -> Right):** For a BST, this visits nodes in sorted order.
    * **Preorder Traversal (Root -> Left -> Right):** Useful for creating a copy of the tree.
    * **Postorder Traversal (Left -> Right -> Root):** Useful for deleting the tree.
* **Search:** Finding a specific value in the tree.

**Implementation of a Binary Search Tree (Simplified Insertion and Inorder Traversal):**

```python
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = BinaryTreeNode(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:  # Duplicate value, usually handled by ignoring or raising error
                return

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def search(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False


# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 50 60 70 80
print("\n")

print("Search for 40:", bst.search(40))  # Output: True
print("Search for 90:", bst.search(90))  # Output: False
```

Binary trees, especially binary search trees, are incredibly efficient for operations like search, insertion, and
deletion ($O(\log N)$ on average for balanced trees), making them vital in databases, file systems, and more.

---
