class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        count = [0]*3
        for i in A:
            count[i] += 1
        s = [sum(count[0:i]) for i in range(1,4)]
        cindex = 0
        for j in range(len(A)):
            while j >= s[cindex]:
                cindex += 1
            A[j] = cindex

A = [0, 1, 0, 2, 0, 1, 0, 1, 1, 2]
print A
sol = Solution()
sol.sortColors(A)
print A
