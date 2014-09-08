import timeit
# given an array of the form abcd1234, change it in-place to a1b2c3d4

class Solution:
    def interplace(self, A):
        self.recursive(A, 0, len(A)-1)
    def recursive(self, A, b, e):
        if e-b == 1: return
        hl = (e+1-b)/2
        upper = hl/2
        lower = hl - upper
        self.reverse(A, b+upper , e-lower)
        self.reverse(A, b+upper, b+upper+upper-1)
        self.reverse(A, b+upper+upper, b+upper+upper+lower-1)
        self.recursive(A, b, b+upper+upper-1)
        self.recursive(A, b+upper+upper, e)
    def reverse(self, A, b, e):
        while b < e:
            A[b], A[e] = A[e], A[b]
            b += 1
            e -= 1
def run():
    sol = Solution()
    A = [i for i in [unichr(i) for i in range(ord('a'), ord('z')+1)]]
    A = A*200
    sol.interplace(A)

print timeit.timeit('run()', setup = "from __main__ import *", number=1)
