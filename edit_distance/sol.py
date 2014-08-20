class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if not word1: return len(word2)
        if not word2: return len(word1)
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0]*l2 for _ in range(l1)]
        for i in range(1, l1):
            dp[i][0] = i
        for j in range(1, l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # delete last char of word1
                    delete = dp[i-1][j] + 1
                    # insert last char of word2
                    insert = dp[i][j-1] + 1
                    # replace
                    replace = dp[i-1][j-1] + 1
                    dp[i][j] = min(delete, insert, replace)
        return dp[-1][-1]
w1 = 'ab'
w2 = 'bc'
sol = Solution()
print sol.minDistance(w1,w2)
