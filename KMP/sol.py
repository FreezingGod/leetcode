class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if not needle: return haystack
        if len(haystack) < len(needle): return None
        ht = self.buildTable(needle)
        print ht
        m = 0
        i = 0
        while m + i < len(haystack):
            if haystack[m+i] == needle[i]:
                i += 1
                if i == len(needle):
                    return haystack[m:]
            else:
                m = m+i-ht[i]
                i = ht[i] if ht[i] >= 0 else 0
        return None
    def buildTable(self, needle):
        ht = [0] * len(needle)
        ht[0] = -1
        if len(needle) > 2:
            for i in range(2, len(needle)):
                if needle[i-1] == needle[ht[i-1]]:
                    ht[i] = ht[i-1]+1
                else:
                    ht[i] = 0
        return ht

sol = Solution()
print sol.strStr("mississippi", "ssiss")
