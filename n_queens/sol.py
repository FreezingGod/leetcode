class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        results = []
        current = []
        def solve(n, i):
            if i == n:
                results.append(current[:])
                return
            noValid = True
            for j in range(n):
                if isValid((i,j), current, n):
                    current.append((i,j))
                    solve(n,i+1)
                    noValid = False
                    current.pop()
            if noValid: return
        def isValid(pos, current, n):
            if not current: return True
            i, j = pos
            for m, n in current:
                if j == n: return False
                if j-n == i-m: return False
                if j-n == m-i: return False
            return True
        solve(n, 0)
        def drawBoard(sol, n):
            sample = '.'*n
            result = []
            for i, j in sol:
                result.append(sample[0:j]+'Q'+sample[j+1:])
            return result
        rtn = []
        for s in results:
            rtn.append(drawBoard(s, n))
        return rtn
sol = Solution()
print sol.solveNQueens(4)
