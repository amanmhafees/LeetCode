class Solution(object):
    def reverseString(self, s):
        n=len(s)
        for i in range(n/2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
            
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        