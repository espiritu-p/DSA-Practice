from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # maximum bitwise is the largest number in the array.
        # AND can only maintain or decrease the number
        max_and = max(nums)

        max_count = 0
        count = 0

        # only count the consecutive appearances of largest number in the array
        for i in range(n):
            if nums[i] == max_and:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max_count or count
