# this solution does not find pivot, modified binary search to suit the changes
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        length = len(A)
        pos = -1
        s, e = 0, length-1
        while s <= e:
            m = s+(e-s)/2
            if A[m] == target:
                pos = m
                break
            if A[m] >= A[s]:
                if A[s] <= target and target <= A[m]:
                    e = m-1
                else:
                    s = m+1
            else:
                if A[m] <= target and target <= A[e]:
                    s = m+1
                else:
                    e = m-1
        return pos

A, t = [3,1], 1
sol = Solution()
print sol.search(A, t)
