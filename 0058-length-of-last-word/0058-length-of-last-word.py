class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        current_length = 0
        prev_space = False
        for i in s:
            if i == ' ' and not prev_space:
                length = current_length
                current_length = 0
                prev_space = True
            elif i != ' ':
                current_length += 1
                prev_space = False
        if i != ' ':
            length = current_length

        return length