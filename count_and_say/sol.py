class Solution:
    # @return a string
    def countAndSay(self, n):
        result = ['1']
        for i in range(1, n):
            s = ''
            lastc = result[-1][0]
            lastcount = 1
            for c in result[-1][1:]:
                if c == lastc:
                    lastcount += 1
                else:
                    s += str(lastcount)
                    s += lastc
                    lastc = c
                    lastcount = 1
            s += str(lastcount)
            s += lastc
            result.append(s)
        print result
        return result[-1]

sol = Solution()
print sol.countAndSay(10)
