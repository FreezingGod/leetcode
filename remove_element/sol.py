class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        p0, p1 = 0, length-1
        count = 0
        while p0 <= p1:
            if A[p0] == elem:
                count += 1
                A[p0], A[p1] = A[p1], A[p0]
                p1 -= 1
            else:
                p0 += 1
        for i in range(count):
            A.pop()
        return length - count
