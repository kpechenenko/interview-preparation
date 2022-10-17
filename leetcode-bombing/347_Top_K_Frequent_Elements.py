class Solution:
    #     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #         cnts = dict()
    #         for n in nums:
    #             cnts[n] = cnts.get(n, 0) + 1;
    #         return sorted(cnts, key = cnts.get, reverse=True)[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = dict()
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1;
        frequences = [[] for _ in range(len(nums) + 1)]
        for n in cnts:
            frequences[cnts[n]].append(n)
        ans = []
        for i in range(len(frequences) - 1, -1, -1):
            for r in frequences[i]:
                if len(ans) < k:
                    ans.append(r)
        return ans
