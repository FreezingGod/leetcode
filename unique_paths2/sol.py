class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m <= 0: return 0
        n = len(obstacleGrid[0])
        if n <= 0: return 0
        mm = [[0]*n for _ in range(m)]
        if obstacleGrid[-1][-1] == 1: return 0
        mm[-1][-1] = 1
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 1 or mm[i+1][n-1] == 0:
                mm[i][n-1] = 0
            else:
                mm[i][n-1] = 1
        for j in range(n-2, -1, -1):
            if obstacleGrid[m-1][j] == 1 or mm[m-1][j+1] == 0:
                mm[m-1][j] = 0
            else:
                mm[m-1][j] = 1
                print m-1, j, mm[m-1][j]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    mm[i][j] = 0
                else:
                    mm[i][j] = mm[i+1][j] + mm[i][j+1]
        print mm
        return mm[0][0]

o = [[0,0],[0,0]]
sol = Solution()
print sol.uniquePathsWithObstacles(o)
