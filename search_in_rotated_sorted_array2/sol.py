class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        result = False
        s, e = 0, len(A)-1
        while s <= e:
            m = s + (e-s)/2
            if target == A[m]:
                result = True
                break
            if A[s] == A[m] and A[m] == A[e]: # worst case, cannot split
                for i in range(s, e+1):
                    if A[i] == target:
                        result = True
                        break
                break
            if A[m] >= A[s]: # first half does not have pivot
                if target >= A[s] and target <= A[m]:
                    e = m-1
                else:
                    s = m+1
            else: # second half does not have pivot
                if target >= A[m] and target <= A[e]:
                    s = m+1
                else:
                    e = m-1
        return result
