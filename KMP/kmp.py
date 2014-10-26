class KMP:
    def isSub(S, W): # return lowest index of S where substring W is found, otherwise return -1
        if not W: return 0
        if not S: return -1
        if len(S) < len(W): return -1
        ft = self.buildFT(W)
        m, i = 0, 0
        while m+i < len(S):
            if S[m+i] == W[i]:
                i += 1
                if i == len(W):
                    return m
            else:
                if ft[i] == -1:
                    m, i = m+1, 0
                else:
                    m = m + i - ft[i]
                    i = ft[i]
        return -1
    def buildFT(W): # build the fault table
        table = [0]*len(W)
        table[0] = -1
        if len(W) <= 2:
            return table[:len(W)]
        i, j = 0, 2
        while j < len(W):
            if W[i] == W[j]:
                i += 1
                table[j] = i
                j += 1
            elif i > 0:
                i = ft[i]
            else:
                table[j] = 0
                j += 1
        return table
