class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 1:
            return [[1]]
        if num_rows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(3, num_rows+1):
            cur = [1]
            prev = ans[-1]
            for j in range(len(prev) - 1):
                cur.append(prev[j] + prev[j+1])
            cur.append(1)
            ans.append(cur)
        return ans

