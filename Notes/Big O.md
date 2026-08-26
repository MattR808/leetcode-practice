# Big O

**Big O = how an algorithm scales as the input size (`n`) increases.**

## Time Complexity

How much **work/time** does the algorithm need?

| Big O | Name | Example |
|---|---|---|
| `O(1)` | Constant | Accessing `nums[0]` |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | One loop through a list |
| `O(n log n)` | Linearithmic | Efficient sorting |
| `O(n²)` | Quadratic | Nested loops |
| `O(2ⁿ)` | Exponential | Some recursive algorithms |

**Best → Worst:**

`O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(2ⁿ)`

## Space Complexity

How much **extra memory** does the algorithm use?

```text
O(1) → Fixed amount of extra memory
O(n) → Extra memory grows with input
```

## Quick Rules

```python
nums[0]                 # O(1)

for x in nums:          # O(n)
    ...

for x in nums:          # O(n²)
    for y in nums:
        ...
```

### Ignore Constants

`O(2n)` → `O(n)`

`O(100n)` → `O(n)`

### Keep the Biggest Term

`O(n² + n)` → `O(n²)`

`O(n³ + n² + n)` → `O(n³)`

## ⭐ When Solving LeetCode

Ask:

> **"As my input gets bigger, how does the amount of work and memory grow?"**

Then write:

```text
Time:  O(?)
Space: O(?)
```