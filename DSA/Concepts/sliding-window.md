# Sliding Window

## Core Idea

Instead of re-examining every subarray from scratch (brute force O(n²)), maintain a
window defined by two pointers — `left` and `right` — and slide it across the array.
The right pointer always expands the window; the left pointer shrinks it when a
constraint is violated. Each element is added and removed at most once → O(n).

---

## Two Flavours

### Fixed-size window

Window size `k` is given. Right and left move together, always `k` apart.

```
nums = [2, 1, 5, 1, 3, 2],  k = 3
       [2, 1, 5] → sum 8
          [1, 5, 1] → sum 7
             [5, 1, 3] → sum 9  ← max
                [1, 3, 2] → sum 6
```

Template:
```python
window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i]        # add incoming element (right side)
    window_sum -= nums[i - k]    # drop outgoing element (left side)
    max_sum = max(max_sum, window_sum)
```

### Variable-size window

Window grows until a constraint breaks, then shrinks from the left until it's satisfied
again. This is what you've been doing.

```python
left = 0
state = ...   # whatever tracks the window's current condition (set, Counter, int...)

for right in range(len(nums)):
    # 1. Expand — add nums[right] to state
    state.add(nums[right])

    # 2. Shrink — while constraint is broken, remove nums[left] and advance left
    while constraint_broken(state):
        state.remove(nums[left])
        left += 1

    # 3. Record — window [left..right] is now valid; update answer
    answer = max(answer, right - left + 1)
```

The `while` vs `if` choice:
- `while` → shrink as much as needed (variable window, constraint can break badly)
- `if` → shrink by exactly one (fixed-size window, or when you know one step is enough)

---

## Your Solved Problems — Traced

### Maximum Erasure Value (LC 1695) — `while` shrink

**Goal:** longest subarray with all unique elements; return its sum.

```python
unique = set()
left = 0
cur_sum = max_sum = 0

for right in range(len(nums)):
    while nums[right] in unique:     # duplicate found — shrink until it's gone
        unique.remove(nums[left])
        cur_sum -= nums[left]
        left += 1
    unique.add(nums[right])
    cur_sum += nums[right]
    max_sum = max(max_sum, cur_sum)
```

Trace on `[4, 2, 4, 5, 6]`:
```
right=0 (4): unique={4},       window=[4],       sum=4
right=1 (2): unique={4,2},     window=[4,2],     sum=6
right=2 (4): 4 IN unique → shrink:
    remove 4 (left=0), sum=2, left=1
    4 not in unique now → add 4
             unique={2,4},     window=[2,4],     sum=6
right=3 (5): unique={2,4,5},   window=[2,4,5],   sum=11
right=4 (6): unique={2,4,5,6}, window=[2,4,5,6], sum=17  ← answer
```

**Why `while` not `if`:** the incoming element might duplicate something several positions
back, so you need to keep shrinking until the duplicate is actually gone.

---

### Fruits Into Baskets (LC 904) — `if` shrink

**Goal:** longest subarray with at most 2 distinct values (fruit types).

```python
d = Counter()
left = 0

for right in range(len(fruits)):
    d[fruits[right]] += 1          # expand — add right element

    if len(d) > 2:                 # constraint broken: 3 distinct types
        d[fruits[left]] -= 1
        if d[fruits[left]] == 0:
            del d[fruits[left]]
        left += 1                  # shrink by exactly 1

return right - left + 1
```

Trace on `[1, 2, 3, 2, 2]`:
```
right=0 (1): d={1:1},       len=1 ✓  window=[1]
right=1 (2): d={1:1,2:1},   len=2 ✓  window=[1,2]
right=2 (3): d={1:1,2:1,3:1}, len=3 ✗
    remove fruits[0]=1 → d={2:1,3:1}, left=1
             d={2:1,3:1},   len=2 ✓  window=[2,3]
right=3 (2): d={2:2,3:1},   len=2 ✓  window=[2,3,2]
right=4 (2): d={2:3,3:1},   len=2 ✓  window=[2,3,2,2]

right - left + 1 = 4 - 1 + 1 = 4
```

**Why `if` not `while`:** adding one element can raise distinct count by at most 1 (from
2 to 3). Removing one element from the left restores it. One shrink step is always enough.

---

## The Core Decision at Each Step

At `right`, ask: **does the window still satisfy the constraint?**

```
Yes → record answer (if tracking max window), move right on
No  → shrink from left until it does, THEN record answer
```

And ask yourself: **am I maximizing or minimizing?**

- **Maximize** window length → expand eagerly, shrink only when forced
- **Minimize** window length → shrink as soon as constraint is satisfied

```python
# Minimize pattern (e.g. smallest window containing all target chars)
for right in range(len(s)):
    state.add(s[right])
    while constraint_satisfied(state):    # shrink while still valid
        answer = min(answer, right - left + 1)
        state.remove(s[left])
        left += 1
```

---

## Choosing Your State Tracker

| Constraint type | State to track | Example |
|----------------|----------------|---------|
| All elements unique | `set` | Maximum Erasure Value |
| At most k distinct values | `Counter` + `len(d)` | Fruits Into Baskets |
| Sum condition | running integer | Minimum Size Subarray Sum |
| Character frequency match | `Counter` diff count | Permutation in String |
| Fixed size | no state needed | Max sum subarray of size k |

---

## Common Mistakes

**1. Recording answer at the wrong place**

Always record AFTER the shrink loop, not before. The window is only valid after you've
restored the constraint.

```python
# WRONG
answer = max(answer, right - left + 1)   # window might still be invalid
while constraint_broken:
    left += 1

# RIGHT
while constraint_broken:
    left += 1
answer = max(answer, right - left + 1)   # window is now guaranteed valid
```

**2. Off-by-one in window size**

Window `[left..right]` inclusive has size `right - left + 1`, not `right - left`.

**3. Forgetting to update state on shrink**

When you move `left`, you must remove `nums[left]` from your state before incrementing:

```python
state.remove(nums[left])   # ← remove BEFORE incrementing
left += 1
```

**4. Using `while` when `if` is enough (or vice versa)**

If adding one element can only violate the constraint by 1 (e.g. distinct count goes 2→3),
use `if`. If it can cause an arbitrary number of violations, use `while`.

---

## When to Reach for Sliding Window

| Signal in the problem | Pattern |
|----------------------|---------|
| "Subarray / substring" | Almost always sliding window or two pointers |
| "Longest / shortest" subarray satisfying X | Variable window |
| "Exactly k" / "at most k" distinct elements | Variable window with Counter |
| "Fixed size k" | Fixed window |
| "Contiguous" elements | Window (non-contiguous → DP or backtracking) |

## What It Won't Solve

Sliding window only works on **contiguous** subarrays/substrings. If the problem involves
picking non-adjacent elements, subsequences, or 2D grids without a clear linear scan order,
reach for DP or backtracking instead.
