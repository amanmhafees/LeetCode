class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        