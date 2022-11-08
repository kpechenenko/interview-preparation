class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        r = []
        reminder = 0
        while i >= 0 or j >= 0 or reminder > 0:
            cur_sum = reminder
            if i >= 0:
                cur_sum += int(a[i])
                i -= 1
            if j >= 0:
                cur_sum += int(b[j])
                j -= 1
            reminder = cur_sum // 2
            cur_mod = cur_sum % 2
            r.insert(0, str(cur_mod))
        return ''.join(r)

