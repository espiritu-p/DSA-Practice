<div align="center">

# DSA Practice

Python solutions to LeetCode and Kattis problems, solved daily.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-27%20Solved-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/)
[![Kattis](https://img.shields.io/badge/Kattis-144%20Solved-1F8ACB?style=flat-square)](https://open.kattis.com/)
[![Last Commit](https://img.shields.io/github/last-commit/espiritu-p/DSA-Practice?style=flat-square&color=brightgreen)](https://github.com/espiritu-p/DSA-Practice/commits/master)

</div>

---

## What this repo is

A daily practice log for algorithms and data structures. Every solution is written in Python with inline comments explaining the approach. Problems come from two sources:

- **LeetCode** — interview-pattern problems, organized by topic and difficulty
- **Kattis** — competitive programming problems, organized by problem type

Alongside the solutions there is a **Concepts** folder with topic-level notes — what the paradigm is, when to use it, and a fully traced example.

---

## Structure

```
DSA-Practice/
├── LeetCode/          solutions grouped by topic
│   ├── Arrays/
│   ├── Bit Manipulation/
│   ├── Greedy/
│   ├── Hashing/
│   ├── Math and String/
│   ├── Sliding Window/
│   ├── Tree and Graph/
│   └── Advanced/
│
├── Kattis/            solutions grouped by problem type
│   ├── Conditionals and Logic/
│   ├── Math and Arithmetic/
│   ├── Simulation/
│   ├── Sorting/
│   └── Strings/
│
└── Concepts/          paradigm notes with worked examples
    ├── dynamic-programming.md
    └── greedy.md
```

---

## Progress

| Source | Solved | Topics covered |
|--------|--------|----------------|
| [LeetCode](./LeetCode/) | 27 | Arrays, Bit Manipulation, Greedy, Hashing, Math & String, Sliding Window, Tree & Graph, Advanced |
| [Kattis](./Kattis/) | 144 | Conditionals & Logic, Math & Arithmetic, Simulation, Sorting, Strings |

---

## Concepts

Concept notes live in [`Concepts/`](./Concepts/). Each file covers one paradigm: the mental model, when to use it, the general template, and a fully traced worked example.

| Concept | Summary |
|---------|---------|
| [Dynamic Programming](./Concepts/dynamic-programming.md) | Break into overlapping subproblems; cache results; optimize via state machine |
| [Greedy](./Concepts/greedy.md) | Take the locally best option at each step; works when local = global optimal |

Progression tracking lives in [`LeetCode/PROGRESS.md`](./LeetCode/PROGRESS.md) — phased topic checklist with per-problem tick boxes.

---

## Problem List (Planned)

A structured set of problems covering patterns most commonly tested in technical interviews. Ordered foundational to advanced within each topic.

<details>
<summary><b>Arrays and Hashing</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy |
| [Missing Number](https://leetcode.com/problems/missing-number/) | Easy |
| [Majority Element](https://leetcode.com/problems/majority-element/) | Easy |
| [Two Sum](https://leetcode.com/problems/two-sum/) | Easy |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium |
| [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium |
| [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium |
| [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium |
| [Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium |

</details>

<details>
<summary><b>Two Pointers</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy |
| [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy |
| [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium |
| [3Sum](https://leetcode.com/problems/3sum/) | Medium |
| [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard |

</details>

<details>
<summary><b>Sliding Window</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy |
| [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium |
| [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium |
| [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard |

</details>

<details>
<summary><b>Stack</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy |
| [Decode String](https://leetcode.com/problems/decode-string/) | Medium |
| [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium |
| [Min Stack](https://leetcode.com/problems/min-stack/) | Medium |
| [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium |
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium |
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium |
| [Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium |
| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard |

</details>

<details>
<summary><b>Binary Search</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy |
| [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium |
| [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium |
| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard |

</details>

<details>
<summary><b>Linked List</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy |
| [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy |
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy |
| [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium |
| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium |
| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium |
| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium |
| [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium |
| [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium |
| [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard |
| [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard |

</details>

<details>
<summary><b>Trees</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy |
| [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy |
| [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy |
| [Same Tree](https://leetcode.com/problems/same-tree/) | Easy |
| [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy |
| [Path Sum](https://leetcode.com/problems/path-sum/) | Easy |
| [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy |
| [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium |
| [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium |
| [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium |
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium |
| [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium |
| [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium |
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard |
| [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard |

</details>

<details>
<summary><b>Tries</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium |
| [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard |

</details>

<details>
<summary><b>Heap / Priority Queue</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy |
| [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy |
| [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Medium |
| [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium |
| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium |
| [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium |
| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard |

</details>

<details>
<summary><b>Backtracking</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium |
| [Subsets](https://leetcode.com/problems/subsets/) | Medium |
| [Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium |
| [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium |
| [Permutations](https://leetcode.com/problems/permutations/) | Medium |
| [Word Search](https://leetcode.com/problems/word-search/) | Medium |
| [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium |
| [N-Queens](https://leetcode.com/problems/n-queens/) | Hard |
| [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard |

</details>

<details>
<summary><b>Graphs</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy |
| [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy |
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium |
| [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium |
| [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium |
| [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium |
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium |
| [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | Medium |
| [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium |
| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium |
| [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium |
| [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium |
| [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard |
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard |

</details>

<details>
<summary><b>Advanced Graphs</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium |
| [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium |
| [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium |
| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard |
| [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard |

</details>

<details>
<summary><b>Dynamic Programming — 1D</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy |
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy |
| [House Robber](https://leetcode.com/problems/house-robber/) | Medium |
| [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium |
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Medium |
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium |
| [Word Break](https://leetcode.com/problems/word-break/) | Medium |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium |
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium |

</details>

<details>
<summary><b>Dynamic Programming — 2D</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium |
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium |
| [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium |
| [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium |
| [Target Sum](https://leetcode.com/problems/target-sum/) | Medium |
| [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium |
| [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard |
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard |
| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard |
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard |

</details>

<details>
<summary><b>Greedy</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium |
| [Jump Game](https://leetcode.com/problems/jump-game/) | Medium |
| [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium |
| [Gas Station](https://leetcode.com/problems/gas-station/) | Medium |
| [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium |
| [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium |
| [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium |
| [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium |
| [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium |
| [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium |

</details>

<details>
<summary><b>Intervals</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy |
| [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium |
| [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard |

</details>

<details>
<summary><b>Bit Manipulation</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Single Number](https://leetcode.com/problems/single-number/) | Easy |
| [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy |
| [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy |
| [Missing Number](https://leetcode.com/problems/missing-number/) | Easy |
| [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium |
| [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium |
| [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium |

</details>

<details>
<summary><b>Math and Geometry</b></summary>
<br>

| Problem | Difficulty |
|---------|-----------|
| [Happy Number](https://leetcode.com/problems/happy-number/) | Easy |
| [Plus One](https://leetcode.com/problems/plus-one/) | Easy |
| [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | Easy |
| [Count Primes](https://leetcode.com/problems/count-primes/) | Medium |
| [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium |
| [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium |
| [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium |
| [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium |
| [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium |
| [Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium |

</details>
