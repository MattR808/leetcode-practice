# Common Data Structures

## 1. List / Array

An ordered collection of items.

```python
nums = [10, 20, 30]

nums[0]       # 10
nums.append(40)
```

**Think:** `[ ]` → things in order

**Typical lookup:** `O(1)` by index

---

## 2. Dictionary / Hash Map

Stores **key → value** pairs.

```python
person = {
    "name": "Matt",
    "age": 22
}

person["name"]    # "Matt"
```

**Think:** `key → value`

**Typical lookup:** `O(1)`

---

## 3. Set / Hash Set

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

**Typical lookup:** `O(1)`

---

## 4. Stack

**Last In → First Out (LIFO)**

Think: **stack of plates**.

```python
stack = []

stack.append(10)
stack.append(20)

stack.pop()    # 20
```

The last thing added is the first thing removed.

---

## 5. Queue

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

---

## 6. Linked List

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

---

## 7. Tree

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

---

## 8. Graph

A collection of **nodes connected by edges**.

```text
A ─── B
│     │
└── C ┘
```

**Think:** maps, networks, social connections.

Graphs can contain cycles and can be directed or undirected.

---

## 9. Heap

A structure designed to quickly access the **smallest or largest** value.

Python uses `heapq` for a min-heap:

```python
import heapq

heap = [5, 2, 8, 1]
heapq.heapify(heap)

heapq.heappop(heap)    # 1
```

**Think:** "give me the smallest item quickly."

---

# ⭐ Learn These First

For LeetCode, focus on these first:

```text
List       → ordered collection
Dictionary → key → value
Set        → unique values
Stack      → LIFO
Queue      → FIFO
```

Then learn:

```text
Linked List → Tree → Heap → Graph
```