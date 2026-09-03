class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices) - 1):
            res = prices[i + 1] - prices[i]
            if res > 0:
                ans += res
        
        return ans
