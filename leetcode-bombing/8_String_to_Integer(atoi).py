class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        while s[i] == ' ':
            i += 1
            if i >= len(s):
                return 0
        is_negative = False
        if s[i] == '-':
            is_negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        d = 1
        num = 0
        for j in range(i - 1, start - 1, -1):
            num += int(s[j]) * d
            d *= 10
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        if is_negative:
            num = -num
        if num < MIN_INT:
            num = MIN_INT
        elif num > MAX_INT:
            num = MAX_INT
        return num


