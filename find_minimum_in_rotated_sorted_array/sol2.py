class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l, r = 0, len(num)-1
        while l < r:
            m = (l+r)/2
            if num[l] <= num[m] and num[m] <= num[r]:
                return num[l]
            if num[l] <= num[m]:
                l = m+1
            else:
                r = m
        return num[l]

sol = Solution()
for i in range(1, 9):
    A = range(i,10)
    A.extend(range(i))
    print A
    print sol.findMin(A)
