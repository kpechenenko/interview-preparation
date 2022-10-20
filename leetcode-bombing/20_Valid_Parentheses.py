class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_brackets = {
            ']': '[',
            ')': '(',
            '}': '{'
        }        
        stack = []
        for ch in s:
            if ch == ']' or ch == ')' or ch == '}':
                if len(stack) == 0 or stack.pop() != close_to_open_brackets[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

