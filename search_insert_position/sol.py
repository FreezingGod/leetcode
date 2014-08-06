class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.mySearch(A, 0, len(A)-1, target)
    def mySearch(self, A, s, e, t):
        if s == e:
            if A[s] == t:
                return s
            elif A[s] > t:
                return s
            else:
                return s+1
        m = (s+e) / 2
        if A[m] == t:
            return m
        elif A[m] < t:
            if m == s:
                m += 1
            return self.mySearch(A, m, e, t)
        else:
            if m == e:
                m -= 1
            return self.mySearch(A, s, m, t)

sol = Solution()
A, t = [1,3,5,6], 5
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 2
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 7
print sol.searchInsert(A, t)
A, t = [1,3,5,6], 0
print sol.searchInsert(A, t)
