class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num: return None
        if len(num) == 1: return num[0]
        l, r = 0, len(num)-1
        while l < r:
            m = (l+r)/2
            if num[l] == num[m] and num[m] == num[r]:
                break
            if num[l] == num[m]:
                if num[m] < num[r]:
                    return num[m]
                else:
                    l = m+1
                    continue
            if num[m] == num[r]:
                if num[l] < num[m]:
                    r = m-1
                else:
                    r = m
                continue
            if num[m] > num[r]:
                l = m+1
            else:
                r = m
        smallest = num[l]
        for i in range(l+1, r+1):
            if num[i] < smallest:
                smallest = num[i]
        return smallest

sol = Solution()
print sol.findMin([1,3,3])
