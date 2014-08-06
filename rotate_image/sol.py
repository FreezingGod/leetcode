# mind how to create 2d list in python
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = matrix[i][j]
        return result

matrix = [[1,2],[3,4]]
sol = Solution()
print sol.rotate(matrix)
