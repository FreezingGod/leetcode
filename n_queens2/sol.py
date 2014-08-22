class Solution:
    # @return an integer
    def totalNQueens(self, n):
        results = [0]
        current = []
        def solve(n, i):
            if i == n:
                results[0] += 1
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
        return results[0]

