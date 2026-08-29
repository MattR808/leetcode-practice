class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        result = sign * int(str(abs(x))[::-1])

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result