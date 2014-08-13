class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if not strs: return []
        dct = {}
        rst = []
        for s in strs:
            srt = ''.join(sorted(s))
            dct[srt] = dct.get(srt, [])
            dct[srt].append(s)
        for k,l in dct.items():
            if len(l) > 1:
                rst.extend(l)
        return rst
strs = ['heart', 'haret']
sol = Solution()
print sol.anagrams(strs)
