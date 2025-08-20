class Solution(object):
    def isPowerOfThree(self, n):
        if n<0 or n==0:
            return False
        x=math.log(n,3)
        return abs(round(x) - x) < 1e-10
        """
        :type n: int
        :rtype: bool
        """
        