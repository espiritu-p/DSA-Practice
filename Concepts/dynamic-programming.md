# Dynamic Programming (DP)

## Core Idea

Break a big problem into smaller subproblems, solve each subproblem once, and store (cache) the result so you never recompute it.

Two properties must hold for DP to apply:

1. **Optimal substructure** — the optimal answer to the big problem can be built from optimal answers to smaller problems.
2. **Overlapping subproblems** — the same smaller problems come up repeatedly (unlike divide-and-conquer where subproblems are independent).

---

## The State Machine Mindset

Most DP problems are easiest to think about as a **state machine**:

- **State**: what information do I need to make a decision at this point?
- **Transition**: what actions move me from one state to another?
- **Value**: what am I maximizing or minimizing?

The DP table stores the best value achievable for every (position, state) combination.

---

## General Template (Bottom-Up)

```python
# 1. Define your states clearly in plain english first
# 2. Write the recurrence (how does state[i] depend on state[i-1]?)
# 3. Set base cases (what is state[0] or state[-1]?)
# 4. Fill the table in order (small subproblems first)
# 5. Read the answer from the final state

dp = {}                         # or a list/2D list depending on dimensions

# base case
dp[base_state] = base_value

for each step in problem:
    dp[current] = max/min(
        dp[previous_option_1],
        dp[previous_option_2],
        ...
    )

return dp[final_state]
```

---

## Worked Example — Best Time to Buy and Sell Stock II

**Problem**: Given daily stock prices, buy and sell unlimited times (hold at most one share at a time). Maximize total profit.

```
prices = [7, 1, 5, 3, 6, 4]
```

### Step 1 — Define States

At the end of any day, you are in exactly one of two states:

- `HOLD` — you are holding a stock right now
- `CASH` — you are holding cash (no stock)

`dp[(day, HOLD)]` = max cash achievable at end of `day` while holding a stock  
`dp[(day, CASH)]` = max cash achievable at end of `day` while NOT holding a stock

### Step 2 — Write Transitions (ask "how did I get here?")

```
dp[day, HOLD] = max(
    dp[day-1, HOLD],           # held yesterday, did nothing today
    dp[day-1, CASH] - price    # had cash yesterday, BOUGHT today
)

dp[day, CASH] = max(
    dp[day-1, CASH],           # had cash yesterday, did nothing today
    dp[day-1, HOLD] + price    # held stock yesterday, SOLD today
)
```

### Step 3 — Base Cases (fictional "day -1" before trading begins)

```
dp[-1, HOLD] = -infinity   # impossible to hold stock before trading starts
dp[-1, CASH] = 0           # start with no profit, no stock
```

Using `-infinity` for the impossible state poisons it — it can never win a `max()`, so the recurrence handles day 0 the same as every other day, no special case needed.

### Step 4 — Trace the Table

```
prices = [7,  1,  5,  3,  6,  4]

day -1:  HOLD=-inf   CASH=0

day 0 (price=7):
  HOLD = max(-inf,  0 - 7) = -7       ← bought at 7
  CASH = max(0,   -inf + 7) = 0       ← -inf can't win

day 1 (price=1):
  HOLD = max(-7,   0 - 1) = -1        ← bought at 1 (better than holding 7)
  CASH = max(0,   -7 + 1) = 0

day 2 (price=5):
  HOLD = max(-1,   0 - 5) = -1        ← keep holding (bought at 1)
  CASH = max(0,   -1 + 5) = 4         ← SOLD at 5, net profit = 4

day 3 (price=3):
  HOLD = max(-1,   4 - 3) = 1         ← bought at 3 (already have 4 profit in hand)
  CASH = max(4,   -1 + 3) = 4

day 4 (price=6):
  HOLD = max(1,    4 - 6) = 1
  CASH = max(4,    1 + 6) = 7         ← SOLD at 6, total profit = 7

day 5 (price=4):
  HOLD = max(1,    7 - 4) = 3
  CASH = max(7,    1 + 4) = 7         ← no better move

Answer = dp[last_day, CASH] = 7
```

Answer is always `CASH` on the last day — an unsold stock earns nothing.

### Step 5 — Code

```python
import math

def maxProfit(prices):
    HOLD, CASH = 0, 1

    dp = {}
    dp[-1, HOLD] = -math.inf   # impossible starting state
    dp[-1, CASH] = 0           # realistic starting state

    for day, price in enumerate(prices):
        dp[day, HOLD] = max(dp[day-1, HOLD], dp[day-1, CASH] - price)
        dp[day, CASH] = max(dp[day-1, CASH], dp[day-1, HOLD] + price)

    return dp[len(prices)-1, CASH]
```

Space-optimized (only need previous day's values):

```python
def maxProfit(prices):
    hold = -math.inf
    cash = 0

    for price in prices:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price)

    return cash
```

> **Note**: compute `new_hold` and `new_cash` from the *old* values each iteration.
> The one-liner above works here because `cash - price` uses the old `cash` before it's overwritten,
> but in problems with more states, always save old values first.

---

## When to Reach for DP

| Signal | Example |
|---|---|
| "Maximum/minimum" over a sequence of choices | Max profit, min cost, longest subsequence |
| Future choices depend on past choices | Can't buy if already holding |
| Brute force is exponential but subproblems repeat | Fibonacci, coin change |
| "How many ways" | Climbing stairs, unique paths |

## When DP is NOT the right tool

- Subproblems are independent → use Divide & Conquer (merge sort)
- Local best is always global best → use Greedy (see `greedy.md`)
- No ordering / state → use BFS/DFS

---

## The Stock Problem Family

This same `HOLD`/`CASH` state machine solves the entire LeetCode stock series.
Only the recurrences change:

| Problem | What changes |
|---|---|
| At most 1 transaction (LC 121) | `HOLD` can only transition from `CASH` once |
| Unlimited transactions (LC 122) | This file — no restriction |
| With cooldown (LC 309) | Add a third state: `COOLDOWN` |
| With transaction fee (LC 714) | Subtract fee on sell transition |
| At most k transactions (LC 188) | Add a transaction-count dimension to state |
