class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers will never be a palindrome
        if x < 0:
            return False

        reverse = 0  # contains the reversed number
        temp = x  # store a copy of x

        while temp != 0:
            x_last_digit = temp % 10  # extract last digit of temp
            reverse = (
                reverse * 10 + x_last_digit
            )  # build reverse num from the ones digit
            temp //= 10  # integer divide temp to remove last number

        return x == reverse
