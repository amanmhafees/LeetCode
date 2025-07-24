class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        sec_num=0
#         for i in range (len(nums)):
#             sec_num=target-nums[i]
#             for j in range(i+1,len(nums)):
#                 if(nums[j]==sec_num):
#                     result.extend([i,j])
#                     return result
        seen={}
        for i,num in enumerate(nums):
            sec_num=target-num
            if sec_num in seen:
                return [seen[sec_num],i]
            seen[num]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        