class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        if len(A) == 1: return 1
        p = 1
        twice = False
        for i in range(1, len(A)):
            if A[i] == A[p-1]:
                if not twice:
                    twice = True
                    A[p] = A[i]
                    p += 1
                else:
                    continue
            else:
                A[p] = A[i]
                twice = False
                p += 1
        return p
A = [1,1,1,1,3,3]
print A
sol = Solution()
print sol.removeDuplicates(A)
print A
