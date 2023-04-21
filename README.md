[![pl](https://img.shields.io/badge/lang-pl-red.svg)](README.pl.md)
[![en](https://img.shields.io/badge/lang-en-green.svg)](README.md)

# Table of Contents

- [Recursion](#recursion)
- [LinkedList](#linkedlist)
  - [LinkedListNode](#linkedlistnode)
  - [LinkedList](#linkedlist-class)
- [Stack](#stack)
- [Queue](#queue)
- [Ceasar](#ceasar)
- [Binary Trees](#binary-trees)
  - [BinaryNode](#binarynode)
  - [BinarySearchTree](#binarysearchtree)
  - [BinaryNode (BT)](#binarynode-bt)
  - [BinaryTree](#binarytree-bt)
- [Graph](#graph)

## Recursion

Recursion is a programming technique where a function calls itself as a subroutine. This allows a problem to be divided into smaller subproblems until a base case is reached, at which point the function stops calling itself and begins to return values.

### Balanced Parentheses

This function checks if a given string contains balanced parentheses (i.e., each opening parenthesis has a corresponding closing parenthesis).

```python
def is_balanced(s: str) -> bool:
    stack = []

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or
               (char == '}' and top != '{') or
               (char == ']' and top != '['):
                return False

    return len(stack) == 0
```

### Combinations

This function calculates the number of combinations (n choose k) using recursion.

```python
def combinations(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)
```

### Factorial

This function calculates the factorial of a given number using recursion.

```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Fibonacci

This function calculates the nth Fibonacci number using recursion.

```python
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Numbers

This function calculates the sum of all numbers from 1 to n using recursion.

```python
def sum_numbers(n: int) -> int:
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
```

### N Sums

This function returns all combinations of n numbers from a list of numbers that add up to a given target.

```python
def n_sums(n: int, target: int, nums: List[int], start: int = 0) -> List[List[int]]:
    if n == 0:
        return [[]] if target == 0 else []
    if start == len(nums):
        return []
    res = []
    for i in range(start, len(nums)):
        num = nums[i]
        for comb in n_sums(n - 1, target - num, nums, i + 1):
            res.append([num] + comb)
    return res
```

## LinkedList

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the list.

### LinkedListNode

LinkedListNode represents a node in a singly linked list, which stores a value and a reference to the next node in the list.

```python
class LinkedListNode:
    def __init__(self, value: Any, next_node: Optional['LinkedListNode'] = None):
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return str(self.value)
```

### LinkedList (class)

The LinkedList class implements a singly linked list with methods to append, insert, delete, and find nodes, as well as other utility methods.

```python
class LinkedList:
    def __init__(self, head: Optional[LinkedListNode] = None):
        self.head = head

    def append(self, value: Any) -> None:
        if not self.head:
            self.head = LinkedListNode(value)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = LinkedListNode(value)

    def insert(self, value: Any, position: int) -> None:
        if position == 0:
            self.head = LinkedListNode(value, self.head)
        else:
            current = self.head
            for _ in range(position - 1):
                if not current:
                    raise IndexError("Position out of range")
                current = current.next_node
            current.next_node = LinkedListNode(value, current.next_node)

    def delete(self, value: Any) -> None:
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def find(self, value: Any) -> Optional[LinkedListNode]:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next_node
        return None

    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def __str__(self) -> str:
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next_node
        return " -> ".join(result)
```

## Stack

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning the last element added to the stack is the first one to be removed.

```python
class Stack:
    def __init__(self):
        self._storage = []

    def push(self, item: Any) -> None:
        self._storage.append(item)

    def pop(self) -> Any:
        if not self._storage:
            raise IndexError("Stack is empty")
        return self._storage.pop()

    def peek(self) -> Any:
        if not self._storage:
            raise IndexError("Stack is empty")
        return self._storage[-1]

    def is_empty(self) -> bool:
        return len(self._storage) == 0

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        return str(self._storage)
```

## Queue

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle, meaning the first element added to the queue is the first one to be removed.

````python
class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    ```python
    def peek(self) -> Any:
        if not self._storage.head:
            raise IndexError("Queue is empty")
        return self._storage.head.value

    def enqueue(self, item: Any) -> None:
        self._storage.append(item)

    def dequeue(self) -> Any:
        if not self._storage.head:
            raise IndexError("Queue is empty")
        value = self._storage.head.value
        self._storage.head = self._storage.head.next_node
        return value

    def is_empty(self) -> bool:
        return self._storage.head is None

    def __len__(self) -> int:
        return self._storage.length()

    def __str__(self) -> str:
        return str(self._storage)
````

## Caesar

The Caesar Cipher is a simple substitution cipher that shifts the letters in the alphabet by a fixed number of positions (key). It is one of the oldest and most widely known encryption techniques.

```python
from string import ascii_lowercase as alphabet

alphabet = [letter for letter in alphabet]

class Ceasar:
    @staticmethod
    def encrypt(text: int, key: int) -> str:
        encrypted_text = ""
        text = text.lower()
        for letter in text:
            if letter in alphabet:
                encrypted_text += alphabet[
                    (alphabet.index(letter) + key) % len(alphabet)
                ]
            else:
                encrypted_text += letter
        return encrypted_text

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        text = text.lower()
        return Ceasar.encrypt(text, -key)

    @staticmethod
    def brute_force(text: str) -> None:
        text = text.lower()
        for key in range(len(alphabet)):
            print(f"Key: {key} - {Ceasar.decrypt(text, key)}")
```

The `Ceasar` class provides three static methods for working with the Caesar Cipher:

- `encrypt(text: int, key: int)`: Encrypts the given text using the Caesar Cipher with the specified key.
- `decrypt(text: str, key: int)`: Decrypts the given text using the Caesar Cipher with the specified key.
- `brute_force(text: str)`: Decrypts the given text using the Caesar Cipher by trying all possible keys (brute-force approach).

## Binary Trees

Binary trees are tree data structures that have at most two child nodes.

### BinaryNode

A binary node is a node in a binary tree, which contains a value and references to left and right children.

```python
class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None
```

### BinarySearchTree

A binary search tree is a binary tree with the property that the value of each node is greater than or equal to the values of all the nodes in its left subtree and less than or equal to the values of all the nodes in its right subtree.

```python
class BinarySearchTree:
    def __init__(self, root: Optional[BinaryNode] = None):
        self.root = root

    def insert(self, value: Any) -> None:
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: BinaryNode, value: Any) -> None:
        if value <= node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = BinaryNode(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = BinaryNode(value)
```

### BinaryNode (BT)

```python
class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None
```

### BinaryTree (BT)

```python
class BinaryTree:
    def __init__(self, root: Optional[BinaryNode] = None):
        self.root = root

    # Additional BinaryTree methods can be added here
```

## Graph

A graph is a data structure consisting of a finite set of vertices (or nodes) and a set of edges connecting them.

```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex: Any) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1: Any, vertex2: Any, bidirectional: bool = True) -> None:
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        if bidirectional:
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1: Any, vertex2: Any, bidirectional: bool = True) -> None:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
        if bidirectional:
            if vertex2 in self.adjacency_list and vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex: Any) -> None:
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                if vertex in self.adjacency_list[v]:
                    self.adjacency_list[v].remove(vertex)

    def __str__(self) -> str:
        result = []
        for vertex, edges in self.adjacency_list.items():
            result.append(f"{vertex}: {', '.join(map(str, edges))}")
        return "\n".join(result)
```
