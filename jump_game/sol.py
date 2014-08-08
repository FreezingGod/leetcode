# this solution use builtin function any
# the time complexiy is O(n^2)
# cannot pass large test set
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        length = len(A)
        result = [False]*length
        result[-1] = True
        for i in range(length-2, -1, -1):
            l = min(length, i+A[i]+1)
            result[i] = any(result[i:l])
        return result[0]
a = [2,3,1,1,4]
b = [3,2,1,0,4]
c = range(25000, -1, -1)

sol = Solution()
print sol.canJump(a)
print sol.canJump(b)
print sol.canJump(c)
