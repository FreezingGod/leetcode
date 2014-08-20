class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        p = self.simplifyPattern(p)
        print p
        return self.myMatch(s, p)
    def myMatch(self, s, p):
        if not s and not p: return True
        if s and not p: return False
        if not s and p:
            if len(p) >= 2 and p[1] == '*':
                return self.myMatch(s, p[2:])
            else:
                return False
        p1, p2 = 0, 0
        l1, l2 = len(s), len(p)
        while p1 < l1 and p2 < l2:
            if p[p2] == '.':
                if p2+1 < l2 and p[p2+1] == '*':
                    for i in range(p1, l1+1):
                        if self.myMatch(s[i:], p[p2+2:]):
                            return True
                    return False
                else:
                    p1 += 1
                    p2 += 1
            else:
                if p2+1 < l2 and p[p2+1] == '*':
                    while p1 < l1 and s[p1] == p[p2]:
                        if self.myMatch(s[p1:], p[p2+2:]):
                            return True
                        else:
                            p1 += 1
                    p2 += 2
                elif s[p1] == p[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
        if p1 < l1: return False
        if p2 < l2:
            while p2 < l2:
                if p2+1 < l2 and p[p2+1] == '*':
                    p2 += 2
                else:
                    break
            if p2 < l2: return False
        return True
    def simplifyPattern(self, p):
        last = ''
        result = ''
        i, l = 0, len(p)
        while i < l:
            if i+1 < l and p[i+1] == '*':
                if len(last) == 2:
                    if last[0] == p[i]:
                        pass
                    elif last[0] == '.' or p[i] == '.':
                        last = '.*'
                    else:
                        result = result + last
                        last = p[i:i+2]
                else:
                    result = result + last
                    last = p[i:i+2]
                i += 2
            else:
                result = result + last
                last = p[i]
                i += 1
        result = result + last
        return result
sol = Solution()
#print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")
#print sol.isMatch("abcd", "d*")
#print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
#print sol.isMatch('aa', 'aa')
print sol.isMatch("bbabacccbcbbcaaab", "a*b*a*a*c*aa*c*bc*")
