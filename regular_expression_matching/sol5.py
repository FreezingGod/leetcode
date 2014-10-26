class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if s and not p: return False
        if not s: return False
        ls, lp = len(s), len(p)
        dp = [[False]*(ls+1) for _ in range(lp+1)]
        dp[0][0] = True
        for i in range(1, lp+1):
            if p[i-1] == '*' and i-2 >= 0:
                dp[i][0] = dp[i-2][0]
        for i in range(1,lp+1):
            for j in range(1, ls+1):
                if p[i-1] == '.' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    if dp[i-1][j] or (i-2>=0 and dp[i-2][j]):
                        dp[i][j] = True
                    elif i-2 >= 0 and (p[i-2] == '.' or p[i-2] == s[j-1]):
                        dp[i][j] = dp[i-1][j-1]
        #for i in range(lp+1):
        #    print dp[i]
        return dp[-1][-1]

sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa")
print sol.isMatch("aaa","aa")
print sol.isMatch("aa", "a*")
print sol.isMatch("aa", ".*")
print sol.isMatch("ab", ".*")
print sol.isMatch("aab", "c*a*b")
