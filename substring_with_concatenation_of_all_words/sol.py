class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result = []
        if not S or not L: return []
        n = len(L)
        l = len(L[0])
        words = set(L)
        count = {}
        for i in L:
            count[i] = count.get(i, 0) + 1
        for i in range(len(S)-n*l+1):
            cc = count.copy()
            success = True
            for j in range(n):
                cw = S[i+j*l:i+(j+1)*l]
                if cw in words:
                    cc[cw] -= 1
                    if cc[cw] < 0:
                        success = False
                        break
                else:
                    success = False
                    break
            if success: result.append(i)
        return result
S = "a"
L = ["a"]
sol = Solution()
print sol.findSubstring(S, L)
