class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.lstrip().strip()
        if not s: return False
        for i in range(len(s)):
            if s[i] == 'e':
                s1 = s[0:i]
                s2 = s[i+1:]
                (a, b) = self.isNum(s1)
                (c, d) = self.isNum(s2)
                if a and c and not d:
                    return True
                else:
                    return False
        (a, b) = self.isNum(s)
        return a

    def isNum(self, s):
        if not s: return (False, False)
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if not s: return (False, False)
        numdots = 0
        for i in range(len(s)):
            if s[i].isdigit():
                continue
            elif s[i] == '.':
                numdots += 1
                if numdots > 1:
                    return (False, False)
            else:
                return (False, False)
        if numdots == 1 and len(s) == 1: return (False, False)
        return (True, numdots==1)
sol = Solution()
print sol.isNumber("e")
