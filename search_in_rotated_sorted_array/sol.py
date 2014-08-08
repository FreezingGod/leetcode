class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        length = len(A)
        pivot = 0
        s,e = 0, length-1
        while s <= e:
            m = s + (e-s)/2
            if A[m] < A[e]:
                if m-1 >= 0 and A[m-1]>A[m]:
                    pivot = m
                    break
                else:
                    e = m-1
            else:
                if m+1 < length and A[m+1]<A[m]:
                    pivot = m+1
                    break
                else:
                    s = m+1
        print pivot
        pos = -1
        if pivot == 0:
            s,e = 0, length-1
        elif target <= A[-1]:
            s,e = pivot, length-1
        else:
            s,e = 0, pivot-1
        while s <= e:
            m = s + (e-s)/2
            if A[m] == target:
                pos = m
                break
            elif A[m] < target:
                s = m+1
            else:
                e = m-1
        return pos

A = [3,1]
target = 1
sol = Solution()
print sol.search(A, target)
