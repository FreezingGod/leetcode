class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A: return 1
        length = len(A)
        for i in range(length):
            while A[i] != i+1 and A[i] >= 1 and A[i] <= length and A[i] != A[A[i]-1]:
                tmp = A[i]
                A[i] = A[A[i]-1]
                A[tmp-1] = tmp
        for i in range(length):
            if A[i] != i + 1:
                return i + 1
        return length + 1
A1 = [3,4,-1,1]
sol = Solution()
print sol.firstMissingPositive(A1)
