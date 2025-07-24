from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=Counter(s)
        n=len(s)
        for i in range(n):
            if(count[s[i]] ==1):
                return i
        return -1
        