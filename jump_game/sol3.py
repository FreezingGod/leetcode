# similar to sol2 but use constant space
class Solution:
     # @param A, a list of integers
     # @return a boolean
    def canJump(self, A):
        length = len(A)
        maxJump = A[0]
        if maxJump >= length-1:
            return True
        for i in range(1, length):
            if maxJump > 0:
                maxJump = max(maxJump-1, A[i])
                if maxJump + i >= length -1:
                    return True
            else:
                return False
        return False
