class Solution:
    # @return a string
    def minWindow(self, S, T):
        if not S or not T: return ''
        if len(S) < len(T): return ''
        expected = {}
        current = {}
        chars = set(i for i in T)
        for i in T:
            expected[i] = expected.get(i,0) + 1
        b, e, m = 0, 0, 10e8
        tcount = 0
        start = 0
        for i in range(len(S)):
            if S[i] in chars:
                current[S[i]] = current.get(S[i], 0) + 1
                if current[S[i]] <= expected[S[i]]:
                    tcount += 1
                if tcount == len(T):
                    while True:
                        if S[start] not in chars:
                            start += 1
                        elif current[S[start]] > expected[S[start]]:
                            current[S[start]] -= 1
                            start += 1
                        else:
                            break
                    if m > i-start+1:
                        b, e, m = start, i, i-start+1
        if m == 10e8:
            return ''
        else:
            return S[b:e+1]

sol = Solution()
print sol.minWindow(S, T)
