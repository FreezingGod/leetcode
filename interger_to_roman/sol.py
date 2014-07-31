class Solution:
    # @return a string
    def intToRoman(self, num):
        s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = ''
        scale = 1000
        idx = len(s) -1
        while num > 0:
            digit = num / scale
            num = num % scale
            scale /= 10
            if digit == 0:
                pass
            elif digit < 4:
                for i in range(digit):
                    result = result + s[idx]
            elif digit == 4:
                result = result + s[idx] + s[idx+1]
            elif digit == 5:
                result = result + s[idx+1]
            elif digit < 9:
                result = result + s[idx+1]
                for i in range(digit-5):
                    result = result + s[idx]
            elif digit == 9:
                result = result + s[idx] + s[idx+2]
            idx -= 2
        return result
sol = Solution()
print sol.intToRoman(3999)
print sol.intToRoman(599)
print sol.intToRoman(438)
