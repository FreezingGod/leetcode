class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        if s and not p: return False
        dp = [[False] * (ls+1) for _ in range(2)]
        current, previous = 0, 1
        dp[current][0] = True
        for i in range(1, lp+1):
            current, previous = previous, current
            dp[current][0] = False
            for j in range(1, ls+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[current][j] = dp[previous][j-1]
                elif p[i-1] == '*':
                    dp[current][j] = dp[previous][j] or dp[previous][j-1] or dp[current][j-1]
        return dp[current][-1]

sol = Solution()

print sol.isMatch("aa","a")
print sol.isMatch("aa","aa")
print sol.isMatch("aaa","aa")
print sol.isMatch("aa", "*")
print sol.isMatch("aa", "a*")
print sol.isMatch("ab", "?*")
print sol.isMatch("aab", "c*a*b")
