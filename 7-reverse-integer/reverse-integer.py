class Solution(object):
    def reverse(self, x):
        res = 0
        limit_low, limit_high = -2**31, 2**31 - 1
        n = abs(x)
        sign = -1 if x < 0 else 1

        while n:
            res = res * 10 + n % 10
            n //= 10

        res *= sign
        return res if limit_low <= res <= limit_high else 0