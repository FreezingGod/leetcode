# use O(m+n) space, not optimal
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        m = len(matrix)
        if not m: return
        n = len(matrix[0])
        if not n: return
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
