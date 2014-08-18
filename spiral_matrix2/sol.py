class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if not n: return []
        result = [[0]*n for _ in range(n)]
        rs, re = 0, n-1
        cs, ce = 0, n-1
        cur = 1
        order = 0
        while rs <= re and cs <= ce:
            if order == 0:
                for i in range(cs, ce+1, 1):
                    result[rs][i] = cur
                    cur += 1
                rs += 1
            elif order == 1:
                for i in range(rs, re+1, 1):
                    result[i][ce] = cur
                    cur += 1
                ce -= 1
            elif order == 2:
                for i in range(ce, cs-1, -1):
                    result[re][i] = cur
                    cur += 1
                re -= 1
            else:
                for i in range(re, rs-1, -1):
                    result[i][cs] = cur
                    cur += 1
                cs += 1
            order += 1
            order = order % 4
        return result
