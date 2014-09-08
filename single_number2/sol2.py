import ctypes
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for i in A:
            zeros = ~(ones | twos)
            twos = (twos & ~i) | (ones & i)
            ones = (ones & ~i) | (zeros & i)
            print i, ones, twos
        print ones, twos
        return ones

A = [1,2,3,3,3, 4,4,4, 2]
A = [1100, 1101, 1101, 1101, 102, 102, 102, 103, 103, 103]
sol = Solution()
print sol.singleNumber(A)
