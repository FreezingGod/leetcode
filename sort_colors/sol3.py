class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A: return
        i, j = 0, len(A)-1
        while i < j:
            while A[i] == 0 and i < j:
                i += 1
            while A[j] != 0 and j > i:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        print A
        i = max(i,j)
        if A[i] == 0:
            i += 1
        j = len(A) - 1
        while i < j:
            while A[i] == 1 and i < j:
                i += 1
            while A[j] == 2 and j > i:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        print A

sol = Solution()
A = [1,0,0]
sol.sortColors(A)
print A
