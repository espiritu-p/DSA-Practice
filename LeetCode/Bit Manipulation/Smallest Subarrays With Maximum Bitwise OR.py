from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        saved_bit_position = [-1] * 31

        # starting from the last element
        for i in range(len(nums) - 1, -1, -1):
            # shortest subarray might be itself
            end_index = i

            # iterate through each bit position
            for cur_bit in range(len(saved_bit_position)):
                # check if current bit is 0
                if (nums[i] & (1 << cur_bit)) == 0:
                    # check if there are set bits already
                    if saved_bit_position[cur_bit] != -1:
                        # update end index where set bit was last seen
                        end_index = max(end_index, saved_bit_position[cur_bit])
                else:
                    saved_bit_position[cur_bit] = i

            ans[i] = end_index - i + 1
        return ans
