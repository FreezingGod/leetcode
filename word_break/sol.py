class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        startidx = [0]
        for i in range(1, len(s)+1):
            for j in startidx:
                if s[j:i] in dict:
                    startidx.append(i)
                    break
        return startidx[-1] == len(s)
