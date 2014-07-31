class Solution:
     # @param A a list of integers
     # @return nothing, sort in place
     def sortColors(self, A):
         p0, p1, p2 = 0, 0, len(A)-1
         while p1 <= p2:
             print p0, p1, p2, A
             if A[p1] == 0:
                 A[p0], A[p1] = A[p1], A[p0]
                 p0 += 1
                 p1 += 1
             elif A[p1] == 2:
                 A[p1], A[p2] = A[p2], A[p1]
                 p2 -= 1
             else:
                 p1 += 1
A = [0, 1, 0, 2, 0, 1, 0, 1, 1, 2]
A = [1,0]
print A
sol = Solution()
sol.sortColors(A)
print A
