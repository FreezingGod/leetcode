class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        si, pi = 0, 0
        laststar, matchindex = -1, -1
        while si < len(s):
            if pi < len(p) and (s[si] == p[pi] or p[pi] == '?'):
                pi += 1
                si += 1
                continue
            if pi < len(p) and p[pi] == '*':
                laststar = pi
                matchindex = si
                pi += 1
                continue
            if laststar != -1:
                pi = laststar + 1
                si = matchindex + 1
                matchindex = si
                continue
            return False
        while pi < len(p) and p[pi] == '*':
            pi += 1
        return pi == len(p)

sol = Solution()
print sol.isMatch("aa", "*")
