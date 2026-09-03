from typing import List
from collections import Counter


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        placed = 0
        d = Counter()

        for i in range(n):
            for j in range(n):
                if baskets[j] >= fruits[i] and d[j] != 1:
                    placed += 1
                    d[j] = 1
                    break

        return len(fruits) - placed
