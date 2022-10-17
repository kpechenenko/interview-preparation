class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for n in nums:
            if n in viewed:
                return True
            else:
                viewed.add(n)
        return False
