class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        n=abs(x)
        while n:
            res=res*10+n%10
            n//=10
        if x<0:
            res=-res
        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res
        