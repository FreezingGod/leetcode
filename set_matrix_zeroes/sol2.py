# this solution does not use any extra space
# it stores the row and column in the first occurance of zero row and zero column
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        if not m: return
        n = len(matrix[0])
        if not n: return
        r,c = -1, -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if r == -1 and c == -1:
                        r,c = i,j
                    else:
                        matrix[r][j] = 0
                        matrix[i][c] = 0
        if r == -1 and c == -1: return
        for i in range(m):
            if matrix[i][c] == 0:
                if i == r:
                    continue
                else:
                    for j in range(n):
                        matrix[i][j] = 0
        for j in range(n):
            if matrix[r][j] == 0:
                if j == c:
                    continue
                else:
                    for i in range(m):
                        matrix[i][j] = 0
        for i in range(m):
            matrix[i][c] = 0
        for j in range(n):
            matrix[r][j] = 0
