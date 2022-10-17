class Solution:
    #     def longestConsecutive(self, nums: List[int]) -> int:
    #         if len(nums) < 2:
    #             return len(nums)
    #         sorted_nums = sorted(nums)
    #         ans = float('-inf')
    #         cur = 1
    #         for i in range(len(sorted_nums) - 1):
    #             if sorted_nums[i + 1] != sorted_nums[i]:
    #                 if abs(sorted_nums[i + 1] - sorted_nums[i]) == 1:
    #                     cur += 1
    #                 else:
    #                     ans = max(ans, cur)
    #                     cur = 1
    #         return max(ans, cur)

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        unique_nums = set(nums)
        longest = float('-inf')
        for n in unique_nums:
            if (n - 1) not in unique_nums:
                cur_len = 1
                while (n + cur_len) in unique_nums:
                    cur_len += 1
                longest = max(longest, cur_len)
        return longest
