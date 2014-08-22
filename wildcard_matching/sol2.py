class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        sp = pp = 0
        star, ss = -1, -1
        while sp < len(s):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
                continue
            if pp < len(p) and p[pp] == '*':
                star = pp
                ss = sp
                pp += 1
                continue
            if star != -1:
                pp = star+1
                sp = ss + 1
                ss = sp
                continue
            return False
        while pp < len(p) and p[pp] == '*':
            pp += 1
        if pp == len(p): return True
        return False
