from typing import List
from collections import Counter
from bisect import bisect_right


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = 0
        fruit_counts = Counter()

        for fruit in fruits:
            fruit_counts[fruit[0]] = fruit[1]

        fruit_idxs = [idx for idx in fruit_counts.keys() if idx != startPos]

        # binary search to check index of startPos in fruit_idxs
        startPos_idx = bisect_right(fruit_idxs, startPos)

        # Get pre-sum of left at each index where fruit can be collected
        left_pre_sum = []
        _left_fruit_count = 0

        # start at the left of startPos index
        for i in range(startPos_idx - 1, -1, -1):
            fruit_idx = fruit_idxs[i]
            _left_fruit_count += fruit_counts[fruit_idx]
            left_pre_sum.append([startPos - fruit_idx, _left_fruit_count])

        # Get pre-sum of right at each index where fruit can be collected
        right_pre_sum = []
        _right_fruit_count = 0

        # start at the right of startPos index
        for i in range(startPos_idx, len(fruit_idxs)):
            fruit_idx = fruit_idxs[i]
            _right_fruit_count += fruit_counts[fruit_idx]
            right_pre_sum.append([fruit_idx - startPos, _right_fruit_count])

        # Collect fruit on the LEFT then move RIGHT
        for distance, fruit_count in left_pre_sum:
            # check if we have enough steps to go left towards distance
            if distance <= k:
                # collect fruits
                cur_fruit_count = fruit_count

                # compute distance that can be covered when moving to the right
                move_right = k - 2 * distance

                # check if we can cover any distance to the right
                if move_right > 0:
                    # binary search on the first element to get index where move_right can be placed
                    idx = bisect_right(right_pre_sum, [move_right, float("inf")])

                    # check if move_right can be placed anywhere other than the first element of right_pre_sum
                    if idx > 0:
                        # add the fruit_count of the index before the position of move_right
                        cur_fruit_count += right_pre_sum[idx - 1][1]

                # update answer
                ans = max(ans, cur_fruit_count)

        # Collect fruit on the RIGHT then move LEFT
        for distance, fruit_count in right_pre_sum:
            # check if we have enough steps to go RIGHT towards distance
            if distance <= k:
                # collect fruits
                cur_fruit_count = fruit_count

                # compute distance that can be covered when moving to the LEFT
                move_left = k - 2 * distance

                # check if we can cover any distance to the LEFT
                if move_left > 0:
                    # binary search on the first element to get index where move_left can be placed
                    idx = bisect_right(left_pre_sum, [move_left, float("inf")])

                    # check if move_left can be placed anywhere other than the first element of left_pre_sum
                    if idx > 0:
                        # add the fruit_count of the index before the position of move_left
                        cur_fruit_count += left_pre_sum[idx - 1][1]

                # update answer
                ans = max(ans, cur_fruit_count)

        # add fruit count at starting position since this was not included yet
        ans += fruit_counts[startPos]

        return ans
