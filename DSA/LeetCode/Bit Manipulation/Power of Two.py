class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool(n) and not (n & n - 1)
