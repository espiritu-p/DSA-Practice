from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        if numRows == 0:
            return ans

        ans.append([1])  # First row is always [1]

        for i in range(1, numRows):
            prev_row = ans[i - 1]

            current_row = [1]  # Always starts with 1

            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)  # Always ends with 1

            ans.append(current_row)

        return ans
