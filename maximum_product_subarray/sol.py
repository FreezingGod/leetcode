class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A: return
        curmax = A[0]
        pmax, nmax = 1, 1
        for i in A:
            if i == 0:
                if curmax < 0:
                    curmax = 0
                pmax = 1
                nmax = 1
            elif i >= 1:
                pmax *= i
                nmax *= i
                if pmax > curmax:
                    curmax = pmax
            else: # i < 0
                if nmax > 0:
                    nmax *= i
                    pmax = 1
                else:
                    onmax, opmax = nmax, pmax
                    nmax = opmax * i
                    pmax = onmax * i
                    if pmax > curmax:
                        curmax = pmax
        return curmax

sol = Solution()
A = [2, 3, -2,  4, -1]
print sol.maxProduct(A)
