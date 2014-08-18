class Solution:
    # @return a string
    def getPermutation(self, n, k):
        candidates = range(1,n+1)
        result = []
        divider = 1
        for i in range(1,n):
            divider *= i
        cur = n-1
        k-=1
        while cur:
            nth = k/divider
            result.append(candidates.pop(nth))
            k = k % divider
            divider /= cur
            cur -= 1
        result.append(candidates.pop())
        return ''.join(str(i) for i in result)
sol = Solution()
print sol.getPermutation(3, 6)
