class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        return self.myRemoveDeplicates(A, 3)
    def myRemoveDeplicates(self, A, max_allow):
        if not A: return 0
        if len(A) == 1: return 1
        p = 1
        lastcount = 1
        for i in range(1, len(A)):
            if A[p-1] == A[i] and lastcount < max_allow:
                lastcount += 1
                A[p] = A[i]
                p += 1
            elif A[p-1] == A[i]:
                continue
            else:
                A[p] = A[i]
                p += 1
                lastcount = 1
        return p
A = [1,1,1,1,3,3]
print A
sol = Solution()
print sol.removeDuplicates(A)
print A
