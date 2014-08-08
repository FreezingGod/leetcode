# this solution gets time limit exceeded
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        length = len(A)
        jumps = [0]*length
        for i in range(length-2, -1, -1):
            jumps[i] = min(jumps[i+1:min(i+1+A[i]+1, length)])+1
        return jumps[0]

A = [2,3,1,1,4]
A = [2,1,3,1,1,4]
sol = Solution()
print sol.jump(A)
