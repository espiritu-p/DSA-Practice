from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        ans = []

        for e in c.most_common(k):
            ans.append(e[0])

        return ans
