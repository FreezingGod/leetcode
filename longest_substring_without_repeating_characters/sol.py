class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        lastidx={}
        longest = 1
        start = 0
        for i in range(len(s)):
            if s[i] in lastidx:
                if lastidx[s[i]]+1 > start:
                    start = lastidx[s[i]]+1
                if i-start+1 > longest:
                    longest = i-start+1
                    print start, i, longest
                    print s[start:(i+1)]
            else:
                if i-start+1 > longest:
                    longest = i-start+1
                    print start, i, longest
                    print s[start:(i+1)]
            lastidx[s[i]] = i
        if len(s)-start> longest:
            longest = len(s) - start
        return longest
sol = Solution()
print sol.lengthOfLongestSubstring("hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac")
