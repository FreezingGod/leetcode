import timeit
# given an array of the form abcd1234, change it in-place to a1b2c3d4

class Solution:
    def interplace(self, A):
        if len(A) == 2: return
        p0, p1 = 1, len(A)/2
        while p0 != p1:
            tmp = A[p1]
            for i in range(p1, p0, -1):
                A[i] = A[i-1]
            A[p0] = tmp
            p0 += 2
            p1 += 1

def run():
    sol = Solution()
    A = [i for i in [unichr(i) for i in range(ord('a'), ord('z')+1)]]
    A = A*200
    sol.interplace(A)
print timeit.timeit('run()', setup = "from __main__ import *", number=1)
