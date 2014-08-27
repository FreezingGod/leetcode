import ctypes
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        threes = 0
        for i in A:
            twos = twos | (ones & i)
            ones = ones ^ i
            threes = ones & twos
            ones = ones & ~threes
            twos = twos & ~threes
            print i, ones, twos, threes
        return ones

A = [1,2,3,3,3, 4,4,4, 2]
sol = Solution()
print sol.singleNumber(A)
