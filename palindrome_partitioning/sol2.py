class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        palin = [[False] * len(s) for _ in range(len(s))]
        palin[-1][-1] = True
        for i in range(len(s)-2, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i < 2 or palin[i+1][j-1]):
                    palin[i][j] = True
        current = []
        result = []
        self.dfs(s, palin, 0, len(s), current, result)
        return result
    def dfs(self, s, palin, start, end, current, result):
        if start == end:
            result.append(current[:])
            return
        for i in range(start, end):
            if palin[start][i]:
                current.append(s[start:i+1])
                self.dfs(s, palin, i+1, end, current, result)
                current.pop()

sol = Solution()
print sol.partition("a")
