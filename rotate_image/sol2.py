# this rotate the matrix in place
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        i1,i2 = 0, n-1
        while i1 < i2:
            matrix[i1],matrix[i2] = matrix[i2],matrix[i1]
            i1 += 1
            i2 -= 1
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
