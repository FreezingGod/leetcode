class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        rst = ''
        length = len(s)
        for i in range(nRows):
            j = 0
            while True:
                idx = i + j*(nRows-1)*2
                if idx < length:
                    rst = rst + s[idx]
                else:
                    break
                if i != 0 and i != nRows-1:
                    idx = idx + (nRows-i-1)*2
                    if idx < length:
                        rst= rst + s[idx]
                    else:
                        break
                j += 1
        return rst
s= "PAYPALISHIRING"
sol = Solution()
print sol.convert(s, 3)
