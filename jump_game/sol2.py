class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        length = len(A)
        jump = [0]*length
        jump[0] = A[0]
        if jump[0] >= length-1:
            return True
        for i in range(1,length):
            if jump[i-1] > 0:
                jump[i] = max(jump[i-1]-1, A[i])
                if jump[i] + i >= length-1:
                    return True
            else:
                return False
        return False
a = [2,3,1,1,4]
b = [3,2,1,0,4]
c = range(25000, -1, -1)
d = [0,1]
e = [0]

sol = Solution()
print sol.canJump(a)
print sol.canJump(b)
print sol.canJump(c)
print sol.canJump(d)
print sol.canJump(e)
