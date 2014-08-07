class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        return self.divide(A, 0, len(A)-1)
    def divide(self, A, s, e):
        if s > e:
            return -10e9
        if s == e:
            return A[s]
        m = s + (e-s)/2
        lmax = self.divide(A, s, m)
        rmax = self.divide(A, m+1, e)
        mlmax, sum = -10e9, 0
        for i in range(m, s-1, -1):
            sum += A[i]
            if sum > mlmax:
                mlmax = sum
        mrmax, sum = -10e9, 0
        for i in range(m+1, e+1):
            sum += A[i]
            if sum > mrmax:
                mrmax = sum
        print lmax, rmax, mlmax+mrmax
        return max([lmax, rmax, mlmax+mrmax])

A = [-2,1]
sol = Solution()
print sol.maxSubArray(A)
