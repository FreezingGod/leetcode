class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l, r = 0, len(A)-1
        while l <= r:
            m = (l+r)/2
            if A[m] == target:
                return m
            #if (m > l and A[m]>target and A[m-1]<target):
            #    return m
            if A[m] > target:
                r = m-1
            else:
                l = m+1
        return l

sol = Solution()
A, t = [1,3,5,6], 5
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 2
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 7
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 0
print sol.searchInsert(A, t)
A, t = [1,3], 0
print sol.searchInsert(A, t)
