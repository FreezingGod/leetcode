class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        if len(A) == 1: return 1
        p0 = 1
        for i in range(1,len(A)):
            if A[p0-1] == A[i]:
                continue
            else:
                A[p0] = A[i]
                p0 += 1
        return p0
