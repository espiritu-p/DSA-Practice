class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        prio_pair = "ab" if x > y else "ba"
        other_pair = "ba" if prio_pair == "ab" else "ab"

        # remove priority pair with higher value
        first_pass = self.remove_pair(s, prio_pair)
        remove_count = (
            len(s) - len(first_pass)
        ) // 2  # divded by two since a pair of characters were removed everytime

        score += remove_count * max(
            x, y
        )  # since the high value pair was removed first, we multiply the remove_count with the max of x and y

        second_pass = self.remove_pair(first_pass, other_pair)
        remove_count = (len(first_pass) - len(second_pass)) // 2

        score += remove_count * min(x, y)

        return score

    def remove_pair(self, input: str, pair: str) -> str:
        char_stack = []

        for cur_char in input:
            if (
                char_stack  # if the stack contains characters
                and cur_char
                == pair[
                    1
                ]  # if the current character is the second character of the pair
                and char_stack[-1]
                == pair[0]  # if the top of the stack is the first character of the pair
            ):
                char_stack.pop()  # remove character from the stack
            else:
                char_stack.append(cur_char)  # keep characters that were not removed

        return "".join(char_stack)
