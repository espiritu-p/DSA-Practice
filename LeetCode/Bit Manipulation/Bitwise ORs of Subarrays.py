from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans, cur = set(), set()

        for i in arr:
            cur = {i | j for j in cur}  # get the bitwise OR of i and j
            cur.add(i)  # add the next number for the next iteration
            ans |= cur  # update ans dictionary

        return len(ans)
