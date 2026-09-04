class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}  # closer -> required opener

        for char in s:
            if char in pairs:
                # Closer with empty stack or mismatched top = invalid
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack  # leftover openers = invalid
