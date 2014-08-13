class Solution:
    # @return a string
    def convert(self, s, nRows):
        rows = [[] for _ in range(nRows)]
        cr = 0
        down = True
        for i in s:
            rows[cr].append(i)
            if down:
                cr += 1
                if cr == nRows:
                    cr -= 2
                    if cr > 0:
                        down = False
            else:
                cr -= 1
                if cr == 0:
                    down = True
        print rows
        rst = ''.join([''.join(i) for i in rows])
        return rst

s= "ABCDEF"
sol = Solution()
print sol.convert(s, 2)
