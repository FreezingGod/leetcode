class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return []
        bits = [0]*n
        change = [True]*n
        result = [0]
        while True:
            success = False
            for i in range(n-1, -1, -1):
                if change[i]:
                    bits[i] = 0 if bits[i] == 1 else 1
                    change[i] = False
                    for i in range(i+1, n):
                        change[i] = True
                    result.append(self.calculate(bits))
                    success = True
                    break
            if not success:
                break
        return result
    def calculate(self, bits):
        result = 0
        for i in bits:
            result = result*2 + i
        return result

sol = Solution()
print sol.grayCode(1)
