# 'a', 'aa' should return ''
# this solution does not handle this case
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if not S or not T: return ''
        chars = set(i for i in T)
        tocover = set(chars)
        idx = {}
        b, e, m = 0, 0, 100000
        for i in range(len(S)):
            if S[i] in chars:
                idx[S[i]] = i
            if S[i] in tocover:
                tocover.remove(S[i])
                if not tocover:
                    nb, ne, char = i, i, ''
                    for c, j in idx.items():
                        if j < nb:
                            nb = j
                            char = c
                    nm = ne-nb+1
                    if nm < m:
                        b,e = nb, ne
                        m = nm
                    tocover.add(char)
        if m == 100000:
            return ''
        else:
            return S[b:e+1]
S = "ADOBECODEBANC"
T = "ABC"
sol = Solution()
print sol.minWindow(S, T)
