class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l = 1
        r = x // 2 + 1
        while l < r:
            m = l + (r - l) // 2
            sq = int(m * m)
            sq_plus_one = int((m + 1) * (m + 1))
            if sq <= x < sq_plus_one:
                return m
            elif sq > x:
                r = m
            else:
                l = m
        return -1

