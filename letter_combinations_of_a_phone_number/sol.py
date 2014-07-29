class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dictionary = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        def dfs(digits, cs):
            if not digits:
                result.append(cs)
                return
            for c in dictionary[int(digits[0])]:
                dfs(digits[1:], cs+c)
        dfs(digits, '')
        return result

s = '23'
sol = Solution()
print sol.letterCombinations(s)
