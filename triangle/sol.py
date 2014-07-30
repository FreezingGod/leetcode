class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        minPath = [10e8] * (len(triangle)+1)
        minPath[1] = 0
        for i in range(1,len(triangle)+1):
            for j in range(i, 0, -1):
                minPath[j] = min(minPath[j], minPath[j-1]) + triangle[i-1][j-1]
        print minPath
        return min(minPath)

sol = Solution()
tri = [ [2], [3,4], [6,5,7], [4,1,8,3] ]
tri = [ [1], [2,3]]
print sol.minimumTotal(tri)
