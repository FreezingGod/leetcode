class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        if s and not p: return False
        dp = [[False] * (ls+1) for _ in range(lp+1)]
        dp[0][0] = True
        flag = False
        for i in range(1, lp+1):
            for j in range(1, ls+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]
        print dp
        return dp[-1][-1]

sol = Solution()

#print sol.isMatch("aa","a")
#print sol.isMatch("aa","aa")
#print sol.isMatch("aaa","aa")
#print sol.isMatch("aa", "*")
#print sol.isMatch("aa", "a*")
#print sol.isMatch("ab", "?*")
print sol.isMatch("aab", "c*a*b")
