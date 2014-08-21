class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l1, l2 = len(A), len(B)
        if l1 <= 2 and l2 <= 2:
            return self.median(A,B)
        p1, p2 = l1 %2, l2%2
        m1, m2 = l1/2, l2/2
        if A[m1] == B[m2]:
            return float(A[m1])
        elif A[m1] < B[m2]:
            A = A[m1:] if p1 else A[m1+1:]
            B = B[0:m2] if p2 else B[0:m2+1]
            return self.findMedianSortedArrays(A, B)
        else:
            A = A[0:m1] if p1 else A[0:m1+1]
            B = B[m2:] if p2 else B[m2+1:]
            return self.findMedianSortedArrays(A, B)
    def median(self, A, B):
        rst = []
        p1, p2 = 0, 0
        while p1 < len(A) and p2 < len(B):
            if A[p1] < B[p2]:
                rst.append(A[p1])
                p1 += 1
            else:
                rst.append(B[p2])
                p2 += 1
        while p1 < len(A):
            rst.append(A[p1])
            p1 +=1
        while p2 < len(B):
            rst.append(B[p2])
            p2 += 1
        l = len(rst)
        if l%2 == 1:
            return float(rst[l/2])
        else:
            return (float(rst[l/2])+float(rst[l/2-1]))/2
sol = Solution()
print sol.findMedianSortedArrays([], [2,3])
