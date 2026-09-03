from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Contruct a set containing positive values then compute for the sum.
        # If it is not possible to create a list with only positive values, it will return a falsy value.
        # This might be the case if the list only contains negative values;
        # If so, simply get the maximum number in the list
        return sum(num for num in {*nums} if num > 0) or max(nums)
