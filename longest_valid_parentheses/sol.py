class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        longest = 0
        dp = [0] * (len(s)+1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                dp[i+1] = 0
            else:
                if not stack:
                    dp[i+1] = 0
                else:
                    idx = stack.pop()
                    dp[i+1] = i-idx+1 + dp[idx]
                    if dp[i+1] > longest:
                        longest = dp[i+1]
        print dp
        return longest

sol = Solution()
print sol.longestValidParentheses("()(()")
