class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        result = [[1]*n for _ in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                result[i][j] = result[i+1][j] + result[i][j+1]
        return result[0][0]
