class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.lstrip().strip()
        if not str: return 0
        negative = False
        if str[0] == '-':
            negative = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        result = 0
        for i in range(len(str)):
            if str[i].isdigit():
                result = result*10 + ord(str[i])-ord('0')
            else:
                break
        if negative:
            result = -result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result

sol = Solution()
print sol.atoi("-1")
