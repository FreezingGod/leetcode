class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if not S or not L: return []
        n = len(L)
        m = len(L[0])
        words = {}
        for i in range(len(L)):
            words[L[i]] = i
        print words
        indicator = [-1]*(len(S)-m+1)
        for i in range(len(indicator)):
            if S[i:i+m] in words:
                indicator[i] = words[S[i:i+m]]
        print indicator
        result = []
        for i in range(len(S)-n*m+1):
            mapped = [False]*n
            failed = False
            for j in range(n):
                val = indicator[j*m+i]
                if val == -1:
                    failed = True
                    break
                else:
                    if mapped[val] == False:
                        mapped[val] = True
                    else:
                        failed = True
                        break
            if not failed:
                result.append(i)
        return result

sol = Solution()
print sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
