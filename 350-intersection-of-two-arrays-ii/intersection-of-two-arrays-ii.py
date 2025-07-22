from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        count1 = Counter(nums1)
        result = []

        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1

        return result
