class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la,lb = len(a)-1,len(b)-1
        c = 0
        result = []
        while la >= 0 or lb >= 0:
            ia, ib = 0, 0
            if la >= 0:
                ia = 1 if a[la] == '1' else 0
            if lb >= 0:
                ib = 1 if b[lb] == '1' else 0
            r = ia + ib + c
            c = 1 if r >= 2 else 0
            r = r % 2
            result.append(r)
            la -= 1
            lb -= 1
        if c: result.append(c)
        result.reverse()
        return ''.join(str(i) for i in result)
