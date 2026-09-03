from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        left_p = 0
        cur_sum = 0
        max_sum = 0

        for right_p in range(len(nums)):
            # before adding to unique set, check if num at right pointer is found at the left pointer
            while nums[right_p] in unique:
                unique.remove(nums[left_p])
                cur_sum -= nums[left_p]
                left_p += 1
            unique.add(nums[right_p])
            cur_sum += nums[right_p]
            max_sum = max(max_sum, cur_sum)

        return max_sum
