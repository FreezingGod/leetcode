class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        longest = 1
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                if i-start > longest:
                    longest = i - start
                    print i, start, longest
                start = max(start, d[s[i]]+1)
                d[s[i]] = i
        if len(s) - start > longest:
            longest = len(s) - start
        return longest

sol = Solution()
print sol.lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")
