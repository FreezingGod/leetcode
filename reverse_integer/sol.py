class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x
        negative = False
        if x < 0:
            negative = True
            x = -x
        digits = []
        while x > 0:
            digits.append(x%10)
            x /= 10
        result = 0
        for d in digits:
            result = result*10 + d
        if negative:
            result = - result
        return result
