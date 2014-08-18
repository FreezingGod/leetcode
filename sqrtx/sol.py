class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0: return None
        if x == 0: return 0
        if x == 1: return 1
        a = 2
        lasta = 2
        while True:
            b = (a + x/a)/2
            if a == b or lasta == b:
                break
            else:
                lasta = a
                a = b
        if a*a >= x:
            if a*a - x <= x - (a-1)*(a-1):
                return a
            else:
                return a-1
        else:
            if x - a*a <= (a+1)*(a+1) - x:
                return a
            else:
                return a+1

sol = Solution()
print sol.sqrt(3)
