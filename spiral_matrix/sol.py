class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix)
        if not m: return result
        n = len(matrix[0])
        if not n: return result
        rs, re = 0, m-1
        cs, ce = 0, n-1
        order = 0
        while rs <= re and cs <= ce:
            if order == 0:
                for i in range(cs, ce+1, 1):
                    result.append(matrix[rs][i])
                rs += 1
            elif order == 1:
                for i in range(rs, re+1, 1):
                    result.append(matrix[i][ce])
                ce -= 1
            elif order == 2:
                for i in range(ce, cs-1, -1):
                    result.append(matrix[re][i])
                re -= 1
            else:
                for i in range(re, rs-1, -1):
                    result.append(matrix[i][cs])
                cs += 1
            order += 1
            order = order % 4
        return result
