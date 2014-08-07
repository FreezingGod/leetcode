class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        result = [[0]*n for _ in range(m)]
        result[m-1][n-1] = grid[m-1][n-1]
        for i in range(m-2, -1, -1):
            result[i][n-1] = result[i+1][n-1] + grid[i][n-1]
        for i in range(n-2, -1, -1):
            result[m-1][i] = result[m-1][i+1] + grid[m-1][i]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                result[i][j] = grid[i][j] + min(result[i+1][j], result[i][j+1])
        return result[0][0]
