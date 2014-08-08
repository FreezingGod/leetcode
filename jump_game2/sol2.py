class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        length = len(A)
        if length <= 1:
            return 0
        jumps, s, e = 0, 0, 0
        while s <= e:
            jumps += 1
            laste = e
            for i in range(s, laste+1):
                newe = max(laste, A[i]+i)
                if newe >= length-1:
                    return jumps
                e = max(e, newe)
            s = laste+1
        return -1

A = [2,1,3,1,1,4]
sol = Solution()
print sol.jump(A)
