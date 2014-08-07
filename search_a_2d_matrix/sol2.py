class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m= len(matrix)
        if not m: return False
        n = len(matrix[0])
        if not n: return False
        if target < matrix[0][0]: return False
        if target > matrix[m-1][n-1]: return False
        s, e = 0, m*n-1
        while s <= e:
            m = s + (e-s)/2
            r,c = m/n,m%n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                s = m + 1
            else:
                e = m - 1
        return False
