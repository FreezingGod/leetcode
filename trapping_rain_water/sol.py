class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        result = 0
        i1, i2 = 0, len(A)-1
        lastH = 0
        while i1 < i2:
            h1,h2 = A[i1],A[i2]
            if h1 > lastH and h2 > lastH:
                newH = min(h1,h2)
                result += (newH-lastH)*(i2-i1+1)
                lastH = newH
            if h1 <= h2:
                i1 += 1
            if h1 >= h2:
                i2 -= 1
        if A[i1] > lastH:
            result += A[i1] - lastH
        return result - sum(A)

A = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print sol.trap(A)
