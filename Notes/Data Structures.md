# Common Data Structures

## 1. List / Array

An ordered collection of items that can be changed.

```python
nums = [10, 20, 30]

nums[0]       # 10

nums.append(40)
```

**Think:** `[ ]` → things in order

**Typical lookup:** `O(1)` by index

**Common operations:**

```python
nums.append(40)     # Add to end
nums.pop()          # Remove last item
nums[0]             # Access by index
len(nums)           # Length
```

---

## 2. Tuple

An **ordered, immutable** collection of items.

```python
my_tuple = (10, 20, 30)

my_tuple[0]       # 10
```

Unlike a list, a tuple **cannot be changed** after it is created.

```python
my_tuple[0] = 50  # Error
```

Tuples can contain different types of data:

```python
person = ("Matt", 22)
```

### Why are tuples useful?

Tuples are **hashable**, so they can be used as dictionary keys.

```python
key = ("a", 1, "b", 2)

my_dict = {}
my_dict[key] = "hello"
```

Lists and dictionaries cannot be dictionary keys because they are mutable.

A useful example:

```python
letter_counts = {"a": 1, "b": 2}

key = tuple(letter_counts.items())
```

**Think:** `( )` → ordered things that don't change

**Typical lookup:** `O(1)` by index

---

## 3. Dictionary / Hash Map

Stores **key → value** pairs.

```python
person = {
    "name": "Matt",
    "age": 22
}

person["name"]    # "Matt"
```

Useful for quickly finding a value using a key.

```python
if "name" in person:
    ...
```

You can add or update values:

```python
person["age"] = 23
person["city"] = "London"
```

**Think:** `key → value`

**Typical lookup:** `O(1)`

**Common uses in LeetCode:**

- Counting things
- Storing relationships
- Looking up values quickly
- Grouping items

Example:

```python
counts = {}

for character in "hello":
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1
```

---

## 4. Set / Hash Set

Stores **unique values**. No duplicates.

```python
nums = {1, 2, 3, 3}

# {1, 2, 3}
```

Useful for quickly checking whether something exists:

```python
if 5 in nums:
    ...
```

Sets automatically remove duplicates:

```python
nums = [1, 2, 2, 3, 3]

unique = set(nums)

# {1, 2, 3}
```

**Think:** `unique values`

**Typical lookup:** `O(1)`

---

## 5. Stack

**Last In → First Out (LIFO)**

Think: **stack of plates**.

```python
stack = []

stack.append(10)
stack.append(20)

stack.pop()    # 20
```

The last thing added is the first thing removed.

### Common operations

```python
stack.append(x)    # Push / add
stack.pop()        # Remove top
stack[-1]          # Look at top
```

**Think:** `LIFO`

Common uses:

- Parentheses
- Undo operations
- Depth-first search
- Backtracking

---

## 6. Queue

**First In → First Out (FIFO)**

Think: **queue at a shop**.

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

queue.popleft()    # 10
```

The first thing added is the first thing removed.

**Think:** `FIFO`

Common uses:

- Breadth-first search
- Processing things in order
- Scheduling

---

## 7. Linked List

A collection of **nodes connected together**.

```text
10 → 20 → 30 → None
```

Each node contains:

```text
[value | next]
```

Example:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Think:** chain of connected nodes.

**Lookup:** `O(n)`

**Insertion/removal:** can be `O(1)` if you already have the relevant node.

---

## 8. Tree

A hierarchical structure made of nodes.

```text
       10
      /  \
     5    15
    / \
   2   7
```

**Think:** family tree.

Common type: **Binary Tree** — each node has at most two children.

Common uses:

- Hierarchical data
- Searching
- File systems
- Binary search trees

---

## 9. Graph

A collection of **nodes connected by edges**.

```text
A ─── B
│     │
└── C ┘
```

**Think:** maps, networks, social connections.

Graphs can contain:

- Cycles
- Directed edges
- Undirected edges
- Weighted edges

Common algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

---

## 10. Heap

A structure designed to quickly access the **smallest or largest** value.

Python uses `heapq` for a **min-heap**:

```python
import heapq

heap = [5, 2, 8, 1]

heapq.heapify(heap)

heapq.heappop(heap)    # 1
```

**Think:** "give me the smallest item quickly."

Common uses:

- Finding the smallest/largest elements
- Priority queues
- Top K problems

---

# ⭐ Learn These First

For LeetCode, focus on these first:

```text
List       → ordered collection
Tuple      → immutable ordered collection
Dictionary → key → value
Set        → unique values
Stack      → LIFO
Queue      → FIFO
```

Then learn:

```text
Linked List → Tree → Heap → Graph
```

---

# 🔑 Useful Python Concepts

## `range()`

```python
for i in range(5):
    print(i)
```

Produces:

```text
0, 1, 2, 3, 4
```

The endpoint is **not included**.

Therefore:

```python
range(len(nums))
```

visits every index:

```text
0 → len(nums) - 1
```

---

## `enumerate()`

Useful when you need both the index and value.

```python
for i, value in enumerate(nums):
    print(i, value)
```

---

## `len()`

Returns the number of items:

```python
len([10, 20, 30])    # 3
```

Remember:

```text
length = 3
last index = 2
```

---

## List Slicing

```python
nums[1:4]
```

Gets indexes:

```text
1, 2, 3
```

The ending index is not included.

---

## `.append()`

Adds an item to the end of a list.

```python
nums = [1, 2]

nums.append(3)

# [1, 2, 3]
```

---

## `.pop()`

Removes and returns an item.

```python
stack = [1, 2, 3]

stack.pop()    # 3
```

With no argument, it removes the last item.

---

## `.items()`

Gets the key-value pairs from a dictionary.

```python
counts = {
    "a": 1,
    "b": 2
}

counts.items()
```

Can be converted to a tuple:

```python
tuple(counts.items())
```

---

## `sorted()`

Sorts an iterable.

```python
letters = ["c", "a", "b"]

sorted(letters)

# ["a", "b", "c"]
```

Can be combined with `.items()`:

```python
sorted(counts.items())
```

This is useful when you need a consistent representation of dictionary contents.

---

# ⭐ Common LeetCode Patterns

```text
Hash Map
    ↓
Counting / lookup / grouping

Set
    ↓
Duplicates / existence checks

Two Pointers
    ↓
Sorted arrays / strings / in-place manipulation

Stack
    ↓
Parentheses / matching / nested structures

Binary Search
    ↓
Sorted data / search space

Sliding Window
    ↓
Subarrays / substrings

BFS / DFS
    ↓
Trees / graphs
```