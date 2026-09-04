class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        # while low and high index haven't passed each other yet
        while low <= high:
            # get the middle index
            mid = (high + low) // 2

            # if we found the target, return the index
            if target == nums[mid]:
                return mid
            # if the target is higher than the current number, set the low index to mid + 1
            elif target > nums[mid]:
                low = mid + 1
            # if the target is lower than the current number, set the high index to mid - 1
            else:
                high = mid - 1

        return -1
