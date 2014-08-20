# TLE
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        p1, p2 = 0, 0
        l1, l2 = len(s), len(p)
        while p1 < l1 and p2 < l2:
            if p2+1 < l2 and p[p2+1] == '*':
                while p1 < l1 and s[p1] == p[p2]:
                    p1 += 1
                p2 += 2
            elif p2 == '.':
                p1 += 1
                p2 += 1
            else:
                if s[p1] == p[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
        if p1 < l1: return False
        if p2 < l2:
            while p2 < l2:
                if p2+1 < l2 and p[p2+1] == '*':
                    p2 += 2
            if p2 < l2: return False
        return True
sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa")
print sol.isMatch("aaa","aa")
print sol.isMatch("aa", "a*")
print sol.isMatch("aa", ".*")
print sol.isMatch("ab", ".*")
print sol.isMatch("aab", "c*a*b")
