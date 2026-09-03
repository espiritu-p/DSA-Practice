# Greedy

## Core Idea

At every step, make the choice that looks best **right now** — without reconsidering past choices or looking ahead.

Greedy is simpler and faster than DP, but it only works when a specific condition holds:

> **The locally optimal choice at each step leads to the globally optimal solution.**

This condition is called the **greedy choice property**. It does NOT always hold — when it doesn't, greedy gives a wrong answer and you need DP or another approach.

---

## Greedy vs DP — The Key Difference

```
DP:     considers ALL possible choices at each step, picks best via recurrence
Greedy: considers ONE choice at each step (the locally best), never revisits
```

| | Greedy | DP |
|---|---|---|
| Speed | Faster (usually O(n) or O(n log n)) | Slower (usually O(n²) or O(nk)) |
| Correctness | Only when greedy choice property holds | Always correct if recurrence is right |
| Code complexity | Simpler | More involved |

---

## General Template

```python
result = 0  # or [], depending on problem

for item in sorted_or_ordered_input:
    if taking item improves result:
        take it
        update result

return result
```

The "trick" is almost always: **sort or scan in the right order** so the greedy choice at each step is unambiguously the best.

---

## Worked Example — Best Time to Buy and Sell Stock II

**Problem**: Given daily stock prices, buy and sell unlimited times. Maximize total profit.

```
prices = [7, 1, 5, 3, 6, 4]
```

### The Greedy Insight

Any profit from holding a stock multiple days equals the sum of the daily gains along the way.

```
Buy day 1 (price=1), sell day 4 (price=6):
  profit = 6 - 1 = 5

That same profit, broken into daily steps:
  day1→day2: 5 - 1 = +4
  day2→day3: 3 - 5 = -2  (would skip this)
  day3→day4: 6 - 3 = +3
  sum of gains = 4 + 3 = 7   ← BETTER than 5 because we dodged the dip

Greedy rule: collect every positive daily gain, skip every loss.
```

This works because buying and selling on the same day is allowed. Holding day 1 → day 4 is mathematically equivalent to three 1-day trades: (1→2) + (2→3) + (3→4). The greedy approach picks only the profitable 1-day trades.

### Trace

```
prices = [7,  1,  5,  3,  6,  4]
           ↕   ↕   ↕   ↕   ↕
changes: -6  +4  -2  +3  -2

Collect only positives:  +4, +3
Total profit = 7  ✓
```

### Code

```python
def maxProfit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:          # tomorrow is higher
            profit += prices[i + 1] - prices[i] # collect today's gain
    return profit
```

One-liner version (same logic):

```python
def maxProfit(prices):
    return sum(
        prices[i+1] - prices[i]
        for i in range(len(prices) - 1)
        if prices[i] < prices[i+1]
    )
```

---

## Classic Greedy Problems (to build intuition)

### Activity Selection / Interval Scheduling

**Problem**: Given intervals, select the maximum number of non-overlapping ones.

**Greedy rule**: always pick the interval that **ends earliest** — it leaves the most room for future picks.

```
Intervals: [(1,4), (2,3), (3,5), (4,6)]

Sort by end time: [(2,3), (1,4), (3,5), (4,6)]

Pick (2,3)  → ends at 3
Skip (1,4)  → starts at 1, overlaps with (2,3)
Pick (3,5)  → starts at 3, no overlap ✓
Pick (4,6)  → starts at 4, overlaps with (3,5) ✗

Result: 2 intervals  ✓
```

### Coin Change (when coins are standard denominations)

**Problem**: Make exact change using fewest coins. Coins: [25, 10, 5, 1]. Amount: 36.

**Greedy rule**: always use the largest coin that fits.

```
36 - 25 = 11  → use quarter
11 - 10 = 1   → use dime
1  - 1  = 0   → use penny
Total: 3 coins  ✓
```

> **Warning**: greedy fails for arbitrary coin sets. Coins [1, 3, 4], amount 6:
> - Greedy: 4+1+1 = 3 coins
> - Optimal: 3+3   = 2 coins ← greedy is wrong here, need DP

### Jump Game (LC 55)

**Problem**: Given `nums[i]` = max jump length from position i, can you reach the end?

**Greedy rule**: track the farthest index reachable. If current index exceeds it, you're stuck.

```python
def canJump(nums):
    reach = 0
    for i, jump in enumerate(nums):
        if i > reach:
            return False        # can't get here
        reach = max(reach, i + jump)
    return True
```

---

## How to Know If Greedy Works

There's no mechanical test — you have to reason about it. But these signals help:

| Signal | Meaning |
|---|---|
| Choices don't affect each other's availability | Greedy usually safe |
| Exchange argument holds ("swapping any two adjacent choices doesn't improve result") | Greedy is provably correct |
| Problem has "unlimited" or "no cap" on actions | Greedy often works |
| Problem has "at most k" or "exactly k" | Often need DP |
| Greedy gives wrong answer on a small example you constructed | Definitely need DP |

**Rule of thumb**: try greedy first, prove or disprove it on small examples. If you can construct a counterexample, switch to DP.

---

## When Greedy Fails — Switch to DP

| Problem | Why greedy fails |
|---|---|
| Coin change with arbitrary denominations | Largest coin can block better combinations |
| 0/1 Knapsack | Taking an item prevents taking it again — future choices affected |
| Stock with at most k transactions | Need to count transactions — state matters |
| Longest increasing subsequence | A longer subsequence might require skipping a locally tempting element |
