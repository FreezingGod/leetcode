class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        l = [len(s) for s in strs]
        minl = min(l)
        ci = 0
        first = strs[0]
        for i in range(minl):
            success = True
            for s in strs[1:]:
                if not first[i] == s[i]:
                    success = False
                    break
            if success:
                ci += 1
            else:
                break
        return first[0:ci]

strs= ['abcdefea', 'abchfalkdsjf', 'abcoeiurq']
sol = Solution()
print sol.longestCommonPrefix(strs)
