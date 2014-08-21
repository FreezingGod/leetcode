class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s or s[0] == '0': return 0
        if len(s) == 1: return 1
        ns = [int(i) for i in s]
        dp = [1,1]
        for i in range(2, len(s)+1):
            if 11 <= ns[i-2]*10 + ns[i-1] <= 26 and ns[i-1] != 0:
                dp.append(dp[i-1] + dp[i-2])
            elif (ns[i-2] == 1 or ns[i-2] == 2) and ns[i-1] == 0:
                dp.append(dp[i-2])
            elif ns[i-1] != 0:
                dp.append(dp[i-1])
            else:
                return 0
        return dp[-1]
