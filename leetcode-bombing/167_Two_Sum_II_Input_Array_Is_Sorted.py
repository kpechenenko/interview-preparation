class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums) - 1
        l = 0
        while l < r:
            cur = nums[l] + nums[r]
            if cur == target:
                return [l+1, r+1]
            elif cur > target:
                r -= 1
            else:
                l += 1
        return []
            
