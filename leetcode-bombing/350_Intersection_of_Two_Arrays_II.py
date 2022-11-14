class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bucket = dict()
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        for n in nums1:
            bucket[n] = bucket.get(n, 0) + 1
        intersection = []
        for n in nums2:
            if n in bucket:
                intersection.append(n)
                bucket[n] -= 1
                if bucket[n] == 0:
                    del bucket[n]
        return intersection

