class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        def myAddress(s, left, cut=[]):
            if len(s) < left or len(s) > left * 3:
                return
            if left == 1:
                val = int(s)
                if val <= 255 and str(val) == s:
                    mycut = cut[:]
                    mycut.append(s)
                    result.append(mycut)
            else:
                for i in range(1,4):
                    mycut = cut[:]
                    mycut.append(s[0:i])
                    val = int(s[0:i])
                    if val <= 255 and str(val) == s[0:i]:
                        myAddress(s[i:], left-1, mycut)
        myAddress(s, 4, [])
        rtn = []
        for l in result:
            rtn.append('.'.join(l))
        return rtn

s = '010010'
sol = Solution()
print sol.restoreIpAddresses(s)
print sol.restoreIpAddresses('25525511135')
