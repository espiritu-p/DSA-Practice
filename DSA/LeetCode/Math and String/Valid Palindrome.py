class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric chars, normalized to lowercase
        clean_s = "".join(char for char in s if char.isalnum()).lower()
        startIdx = 0
        endIdx = len(clean_s) - 1

        # Two pointers closing in from both ends
        while (startIdx < endIdx):
            if clean_s[startIdx] != clean_s[endIdx]:
                return False
            else:
                startIdx+=1
                endIdx-=1

        return True
