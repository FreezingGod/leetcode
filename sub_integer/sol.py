# given two integers a and b of length m and n, where n <= m, check if b is a substring of a if both number are converted to string

class Solution:
    # param: a, b integer
    # param: m, n length of a, b
    # returns a boolean
    def isSub(self, a, b, m, n):
        divisor = 1
        for i in range(n):
            divisor *= 10
        x = m - n + 1
        for i in range(x):
            if a % divisor == b:
                return True
            a /= 10
        return False

sol = Solution()
print sol.isSub(987654321, 654, 9, 3)
