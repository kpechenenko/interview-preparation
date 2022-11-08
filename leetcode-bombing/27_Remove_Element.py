class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = nums.count(val)
        if k == 0:
            return len(nums)
        l = 0
        r = len(nums) - 1
        len_of_clear_nums = len(nums) - k
        while l < len_of_clear_nums:
            if val == nums[l]:
                while val == nums[r]:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return len_of_clear_nums

