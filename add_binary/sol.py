class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a: return b
        if not b: return a
        l = min(len(a), len(b))
        c = 0
        result = []
        for i in range(-1, -l-1, -1):
            i1,i2 = int(a[i]), int(b[i])
            r = i1+i2+c
            if r >= 2:
                r = r % 2
                c = 1
            else:
                c = 0
            result.append(r)
        if len(a) > l:
            for i in range(len(a)-l-1, -1, -1):
                i1 = int(a[i])
                r = i1 + c
                if r >=2:
                    r = r % 2
                    c = 1
                else:
                    c = 0
                result.append(r)
        elif len(b) > l:
            for i in range(len(b)-l-1, -1, -1):
                i1 = int(b[i])
                r = i1 + c
                if r >=2:
                    r = r%2
                    c = 1
                else:
                    c = 0
                result.append(r)
        if c == 1:
            result.append(c)
        result.reverse()
        return ''.join(str(i) for i in result)
a = "11"
b = "1"
sol = Solution()
print sol.addBinary(a,b)
