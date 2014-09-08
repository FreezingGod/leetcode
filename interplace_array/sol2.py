# given an array of the form abcd1234, change it in-place to a1b2c3d4

class Solution:
    def interplace(self, A):
        self.recursive(A, 0, len(A))
    def recursive(self, A, start, length):
        if length - start == 2: return
        p0, p1 = start, start+(length-start)/2
        tmp = A[p1]
        for i in range(p1, p0+1, -1):
            A[i] = A[i-1]
        A[p0+1] = tmp
        self.recursive(A, start+2, length)

sol = Solution()
A = [i for i in 'abcdefg1234567']
print ''.join(A)
sol.interplace(A)
print ''.join(A)
