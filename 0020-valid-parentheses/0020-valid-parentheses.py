class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) ==  1:
            return False
        stack = []
        opening_brackets_set = set(['(', '{', '['])
        closing_brackets_set = set([')', '}', ']'])
        brackets_dict = {'(' : ')', '{': '}', '[': ']'}
        stack.append(s[0])
        for i in s[1:]:
            if i in opening_brackets_set:
                stack.append(i)
            elif i in closing_brackets_set:
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if top_element not in opening_brackets_set:
                    return False
                if brackets_dict[top_element] != i:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True