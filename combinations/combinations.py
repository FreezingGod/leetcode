class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        lst = range(1, n+1)
        rst = []
        for l in self.mycombine(lst, k):
            rst.append(l)
        return rst
    def mycombine(self, lst, k):
        if len(lst) < k:
            return
        if k == 1:
            for i in lst:
                yield [i]
        for i in range(len(lst)):
            for rst in self.mycombine(lst[i+1:], k-1):
                yield [lst[i]] + rst

sol = Solution()
print sol.combine(5,3)
