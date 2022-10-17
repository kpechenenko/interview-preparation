class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = dict()
        for i, n in enumerate(nums):
            reminder = target - n
            if reminder in viewed:
                return [viewed[reminder], i]
            else:
                viewed[n] = i
        return []
