class Solution(object):
    def reverse(self, x):
        res = 0
        n, sign = abs(x), 1 if x >= 0 else -1
        while n:
            res = res * 10 + n % 10
            n //= 10
        res *= sign
        return res if -2**31 <= res <= 2**31 - 1 else 0