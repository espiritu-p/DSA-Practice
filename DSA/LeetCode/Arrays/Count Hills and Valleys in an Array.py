from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        total = 0

        # ignore start and last index
        for i in range(1, len(nums) - 1):
            left_p = i
            right_p = i

            # skip if current number is equal to the previous one
            if nums[i] == nums[i - 1]:
                continue

            # get a number on the left where it is not equal to current number
            while nums[left_p] == nums[i] and left_p != 0:
                left_p -= 1

            # get a number on the right where it is not equal to current number
            while nums[right_p] == nums[i] and right_p != len(nums) - 1:
                right_p += 1

            # count whether current number is a hill or valley
            if (
                nums[left_p] > nums[i]
                and nums[right_p] > nums[i]
                or nums[left_p] < nums[i]
                and nums[right_p] < nums[i]
            ):
                total += 1

        return total
