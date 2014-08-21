class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s: return 0
        dp = [0]*(len(s)+1)
        ns = [int(i) for i in s]
        dp[-1] = 1
        dp[-2] = 1 if ns[-1] != 0 else 0
        if len(s) < 2:
            return dp[0]
        for i in range(len(s)-2, -1, -1):
            if ns[i] == 0:
                if ns[i+1] == 0:
                    return 0
                dp[i] = 0
            else:
                if ns[i+1] == 0 and ns[i] > 2:
                    return 0
                elif ns[i+1] == 0 and ns[i] <= 2:
                    dp[i] = dp[i+2]
                elif i + 2 < len(s) and ns[i+2] == 0:
                    dp[i] = dp[i+1]
                else:
                    if ns[i]*10+ns[i+1] <= 26:
                        dp[i] = dp[i+1]+dp[i+2]
                    else:
                        dp[i] = dp[i+1]
        return dp[0]
sol = Solution()
print sol.numDecodings('12121')
