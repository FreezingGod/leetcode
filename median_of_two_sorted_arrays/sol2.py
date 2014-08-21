class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if (m+n)%2 == 1:
            return float(self.findKth(A,B,(m+n)/2+1))
        else:
            return (self.findKth(A,B,(m+n)/2) + self.findKth(A,B,(m+n)/2+1))/2.0
    def findKth(self,A,B,k):
        m, n = len(A), len(B)
        if m == 0: return B[k-1]
        if n == 0: return A[k-1]
        if k == 1: return min(A[0], B[0])
        if m < n:
            return self.findKth(B, A, k)
        ib = min(k/2, n)
        ia = k - ib
        if A[ia-1] == B[ib-1]:
            return A[ia-1]
        elif A[ia-1] < B[ib-1]:
            return self.findKth(A[ia:], B, k-ia)
        else:
            return self.findKth(A, B[ib:], k-ib)
sol = Solution()
print sol.findMedianSortedArrays([1,3,5,7],[2,4,6,8])
