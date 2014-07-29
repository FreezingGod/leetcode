class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        def gen(n, count, s):
            if n == 0 and count == 0:
                result.append(s)
                return
            if n > 0:
                gen(n-1, count+1, s+'(')
            if count > 0:
                gen(n, count-1, s+')')
        gen(n, 0, '')
        return result

sol = Solution()
print sol.generateParenthesis(3)
