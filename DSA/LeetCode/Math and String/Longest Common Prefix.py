from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)

        first_word = strs[0]
        last_word = strs[-1]

        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return ans

            ans += first_word[i]

        return ans
