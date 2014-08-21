class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        negative = False
        if divisor < 0:
            divisor = -divisor
            negative = not negative
        if dividend < 0:
            dividend = -dividend
            negative = not negative
        result = self.mydivide(dividend, divisor, 0)
        if negative: result = -result
        return result
    def mydivide(self, dividend, divisor, cur):
        result = cur
        if dividend < divisor:
            return result
        cur, value = 1, divisor
        while value + value < dividend:
            cur = cur + cur
            value = value + value
        if value == dividend:
            return result + cur
        else:
            return self.mydivide(dividend-value, divisor, result+cur)

sol = Solution()
print sol.divide(5,2)
