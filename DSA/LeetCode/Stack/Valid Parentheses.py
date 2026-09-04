class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            # if the parentheses are open, append to stack
            if char in "({[":
                stack.append(char)
            # return false if one of the two are true:
            # 1. Check if stack is empty while we're still checking for valid parenthesis
            # 2. If the closing parenthesis does not match the popped parenthesis from the stack
            elif not stack or stack.pop() != pairs[char]:
                return False

        return not stack
