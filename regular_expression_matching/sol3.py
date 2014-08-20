class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        l1, l2 = len(s), len(p)
        dp = [[False]*(l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        for i in range(1, l2+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if p[i-1] == '*':
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] = dp[i-2][j-1] or dp[i-2][j] or dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                else:
                    if p[i-1] == s[j-1] or p[i-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[l2][l1]
sol = Solution()
#print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")
#print sol.isMatch("abcd", "d*")
#print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
#print sol.isMatch('aa', 'aa')
#print sol.isMatch("bbabacccbcbbcaaab", "a*b*a*a*c*aa*c*bc*")
print sol.isMatch('aaa', '.*')
print sol.isMatch("aab", "b.*")
