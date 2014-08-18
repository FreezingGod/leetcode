class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if not num1 or not num2: return ''
        partial = []
        short, other = None, None
        if len(num1) <= len(num2):
            short = num1
            other = num2
        else:
            short = num2
            other = num1
        for i in range(len(short)-1, -1, -1):
            if short[i] != '0':
                n = self.mult(other, ord(short[i])-ord('0'))
                n = n + '0'*(len(short)-i-1)
                partial.append(n)
        if not partial: return '0'
        return self.addlist(partial)
    def mult(self, num1, n2): # n2 is a 1 digit number
        carry = 0
        res = ''
        for i in range(len(num1)-1, -1, -1):
            cd = (ord(num1[i]) - ord('0')) * n2
            cd += carry
            carry = 0
            if cd >= 10:
                carry = cd / 10
                cd = cd % 10
            res = str(cd) + res
        if carry:
            res = str(carry) + res
        return res
    def addlist(self, l):
        if not l: return ''
        length = len(l)
        if length <= 1: return l[0]
        if length <= 2: return self.add(l[0], l[1])
        m = length/2
        return self.add(self.addlist(l[0:m]), self.addlist(l[m:]))
    def add(self, num1, num2):
        res = ''
        if not num1: return num2
        if not num2: return num1
        carry = 0
        l1, l2 = len(num1)-1, len(num2)-1
        while l1 >= 0 and l2 >= 0:
            cd = ord(num1[l1]) + ord(num2[l2]) - ord('0')*2 + carry
            carry = 0
            if cd >= 10:
                carry = cd / 10
                cd = cd % 10
            res = str(cd) + res
            l1 -= 1
            l2 -= 1
        while l1 >= 0:
            cd = ord(num1[l1]) - ord('0') + carry
            carry = 0
            if cd >= 10:
                carry = cd / 10
                cd = cd % 10
            res = str(cd) + res
            l1 -= 1
        while l2 >= 0:
            cd = ord(num2[l2]) - ord('0') + carry
            carry = 0
            if cd >= 10:
                carry = cd / 10
                cd = cd % 10
            res = str(cd) + res
            l2 -= 1
        if carry:
            res = str(carry) + res
        return res
s1 = '123'
s2 = '456'
sol = Solution()
print sol.multiply(s1,s2)
