class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        for i in range(m-1, -1, -1):
            A[i+n] = A[i]
        i1, i2, ci = n, 0, 0
        while i1 < m+n and i2 < n:
            if A[i1] <= B[i2]:
                A[ci] = A[i1]
                i1 += 1
            else:
                A[ci] = B[i2]
                i2 += 1
            ci += 1
        while i2 < n:
            A[ci] = B[i2]
            ci += 1
            i2 += 1

A = [1,3,5,7,8,15]
B = [2,4,6,9,10,11]
A.extend([0]*len(B))
print A,B
sol = Solution()
sol.merge(A,len(A)-len(B), B, len(B))
print A
