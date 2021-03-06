class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        ls, lp = len(s)+1, len(p)+1
        dp = [[False]*ls for _ in range(lp)]
        dp[0][0] = True
        for i in range(1,lp):
            for j in range(1,ls):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa")
print sol.isMatch("aaa","aa")
print sol.isMatch("aa", "*")
print sol.isMatch("aa", "a*")
print sol.isMatch("ab", "?*")
print sol.isMatch("aab", "c*a*b")
