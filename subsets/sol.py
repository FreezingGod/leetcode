class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S: return []
        S.sort()
        result = []
        current = []
        self.dfs(result, current, S)
        return result
    def dfs(self, result, current, S):
        result.append(current[:])
        if len(S) == 0:
            return
        for i in range(len(S)):
            current.append(S[i])
            self.dfs(result, current, S[i+1:])
            current.pop()

sol = Solution()
print sol.subsets([0, 1])
