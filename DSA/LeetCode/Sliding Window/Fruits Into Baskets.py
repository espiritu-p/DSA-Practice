from typing import List
from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = Counter()
        left_p = 0

        for right_p in range(len(fruits)):
            d[fruits[right_p]] += 1

            if len(d) > 2:
                d[fruits[left_p]] -= 1

                if d[fruits[left_p]] == 0:
                    d.pop(fruits[left_p])
                left_p += 1

        return right_p - left_p + 1
