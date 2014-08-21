class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        result = []
        current = []
        def dfs(s, d, current):
            if s == '':
                result.append(' '.join(current))
                return
            for i in range(1,len(s)+1):
                if s[0:i] in d:
                    current.append(s[0:i])
                    d.remove(s[0:i])
                    dfs(s[i:], d, current)
                    current.pop()
                    d.append(s[0:i])
        dfs(s, dict, current)
        return result
s,d= "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
sol = Solution()
print sol.wordBreak(s, d)
