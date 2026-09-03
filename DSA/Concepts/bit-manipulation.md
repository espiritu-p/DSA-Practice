# Bit Manipulation

## Core Idea

Every integer is stored in binary — a sequence of 0s and 1s. Bit manipulation lets you
operate directly on those bits instead of using arithmetic. The payoff is speed (single
CPU instruction) and elegance (problems that look complex reduce to one line).

---

## The Six Operators

| Operator | Symbol | What it does | Example (4-bit) |
|----------|--------|-------------|-----------------|
| AND | `&` | 1 only where BOTH bits are 1 | `1100 & 1010 = 1000` |
| OR | `\|` | 1 where EITHER bit is 1 | `1100 \| 1010 = 1110` |
| XOR | `^` | 1 where bits are DIFFERENT | `1100 ^ 1010 = 0110` |
| NOT | `~` | Flip every bit | `~1100 = 0011` (+ sign flip) |
| Left shift | `<<` | Shift bits left, fill 0s on right | `0011 << 1 = 0110` (×2) |
| Right shift | `>>` | Shift bits right, drop rightmost | `1100 >> 1 = 0110` (÷2) |

**Left shift = multiply by 2. Right shift = divide by 2 (integer).**

```
1 << 0 = 1
1 << 1 = 2
1 << 2 = 4
1 << 3 = 8
1 << k = 2^k
```

---

## The Tricks You Need to Know

### 1. Check if a bit is set at position k

```python
if n & (1 << k):   # is bit k a 1?
```

`1 << k` makes a mask with only bit k set. AND with `n` — if the result is non-zero,
that bit was 1.

```
n     = 1 0 1 1  (11)
mask  = 0 0 1 0  (1 << 1 = 2, checking bit 1)
n & m = 0 0 1 0  → non-zero → bit 1 IS set
```

### 2. Set a bit (force it to 1)

```python
n | (1 << k)
```

### 3. Clear a bit (force it to 0)

```python
n & ~(1 << k)
```

### 4. Toggle a bit (flip it)

```python
n ^ (1 << k)
```

### 5. n & (n-1) — strip the lowest set bit

This is the single most used trick. `n - 1` flips the rightmost 1 and all trailing 0s:

```
n     = 1 0 1 1 0 0  (44)
n - 1 = 1 0 1 0 1 1  (43)
n & (n-1) = 1 0 1 0 0 0  (40)  ← lowest 1 stripped
```

**Use case:** count set bits by repeatedly stripping them.  
**Use case:** check power of two — a power of two has exactly one set bit, so `n & (n-1) == 0`.

### 6. XOR cancellation — `a ^ a = 0`, `a ^ 0 = a`

XOR-ing a value with itself always gives 0. XOR-ing with 0 keeps the value.  
**Use case:** find the one element that appears an odd number of times — XOR everything
together, the even-count elements cancel out.

```python
nums = [2, 3, 2, 4, 4]
result = 0
for n in nums:
    result ^= n   # 0^2^3^2^4^4 = 3
# result = 3  (the only odd-count element)
```

---

## Your Solved Problems — Explained Through These Tricks

### Power of Two (LC 231)

```python
return bool(n) and not (n & n - 1)
```

A power of two in binary has exactly one `1` bit: `1`, `10`, `100`, `1000`, ...  
`n & (n-1)` strips that one bit → result is `0` → `not 0` is `True`.  
The `bool(n)` guard handles `n = 0` (zero is not a power of two but `0 & -1 = 0`).

```
n=8:  1 0 0 0
n-1=7:0 1 1 1
AND:  0 0 0 0  ✓ power of two

n=6:  0 1 1 0
n-1=5:0 1 0 1
AND:  0 1 0 0  ✗ not power of two
```

### Longest Subarray With Maximum Bitwise AND (LC 2419)

Key insight in your solution: AND can only maintain or decrease a value — `x & y <= x`
always. So the maximum possible AND of any subarray is just `max(nums)` (a subarray of
length 1 containing only that element). The answer is the longest consecutive run of
that maximum value.

```
nums = [1, 2, 3, 3, 2, 2]
max  = 3
runs of 3: [3, 3] → length 2
```

### Bitwise ORs of Subarrays (LC 898)

OR can only maintain or increase a value — `x | y >= x` always. Your solution uses a
set `cur` that tracks all distinct OR values achievable ending at the current index.
Because OR is monotonically non-decreasing, `cur` has at most `log(max_val)` distinct
values (each new OR sets at least one new bit, and there are only 30 bits in an int).

```python
cur = {i | j for j in cur}  # extend every previous OR with the new element
cur.add(i)                   # also the subarray of just this element
ans |= cur                   # accumulate all seen values
```

### Count Number of Maximum Bitwise-OR Subsets (LC 2044)

Uses the same OR-monotonicity insight but now counts *how many* subsets reach the max OR.
The `Counter` DP maps `or_value → number of subsets producing it`. For each new number,
every existing subset either includes or excludes it — including it ORs the running value
with `num`. The final answer is `dp[max_or]`.

---

## Common Patterns — Quick Reference

| Goal | Code | Notes |
|------|------|-------|
| Is bit k set? | `n & (1 << k)` | Returns 0 or non-zero |
| Set bit k | `n \| (1 << k)` | Forces bit to 1 |
| Clear bit k | `n & ~(1 << k)` | Forces bit to 0 |
| Toggle bit k | `n ^ (1 << k)` | Flips bit |
| Strip lowest set bit | `n & (n - 1)` | Core of many tricks |
| Is power of two? | `n > 0 and not (n & n-1)` | Exactly one bit set |
| Count set bits | loop with `n & (n-1)` | Or `bin(n).count('1')` |
| Find unique element | XOR all elements | Pairs cancel to 0 |
| Multiply by 2^k | `n << k` | |
| Integer divide by 2^k | `n >> k` | |

---

## When to Reach for Bit Manipulation

- Problem mentions powers of two, odd/even counts, XOR, OR, AND over subsets/subarrays
- Need to represent a set of booleans compactly (bitmask DP)
- Counting set bits, finding unique element, checking flags
- Subarray OR/AND problems — use the monotonicity property

## What It Won't Solve

Bit tricks are local — they operate on individual numbers. They don't replace graph
traversal, DP over sequences, or sorting. If the problem structure is relational (depends
on ordering or position between many elements), bit manipulation is at most a helper, not the core approach.
