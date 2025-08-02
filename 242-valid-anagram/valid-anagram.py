from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        count_s=Counter(s)
        count_t=Counter(t)
        if(count_t==count_s):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        