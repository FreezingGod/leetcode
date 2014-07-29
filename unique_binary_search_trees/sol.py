class Solution:
    # @return an integer
    def numTrees(self, n):
        nTrees = [1,1,2]
        for i in xrange(3, n+1):
            num = 0
            for j in range(i):
                num += nTrees[j]*nTrees[i-j-1]
            nTrees.append(num)
        return nTrees[n]

sol = Solution()
print sol.numTrees(1)
print sol.numTrees(3)
print sol.numTrees(4)
print sol.numTrees(5)
print sol.numTrees(6)
