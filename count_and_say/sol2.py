# this solution use less space than sol
class Solution:
    # @return a string
    def countAndSay(self, n):
        last = '1'
        for i in range(1, n):
            s = ''
            lastc = last[0]
            lastcount = 1
            for c in last[1:]:
                if c == lastc:
                    lastcount += 1
                else:
                    s += str(lastcount)
                    s += lastc
                    lastc = c
                    lastcount = 1
            s += str(lastcount)
            s += lastc
            last = s
        return last
