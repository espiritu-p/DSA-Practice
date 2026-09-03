from typing import List
from collections import Counter

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])
        
        for num in nums:
            # store values in temporary counter to avoid double-counting
            _temp = Counter()

            # for each key-value pair in dp items, update the bitwise OR counter
            # key = bitwise OR result of two numbers
            # value = number of subsets that could get the same bitwise OR result
            for k, v in dp.items():
                _temp[k | num] += v
            
            # if key is already in dp, update the counter of that element
            # if not, include the temp key-value pair into dp
            dp += _temp

        # get max key (bitwise OR result) found in dp and return its value
        return dp[max(dp)]