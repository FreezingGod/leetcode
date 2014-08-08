class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        length = len(A)
        s,e = 0, length-1
        result = [-1,-1]
        while s <= e:
            m = s + (e-s)/2
            if A[m] == target:
                if m-1 >= s:
                    if A[m-1] != target:
                        result[0] = m
                        break
                    else:
                        e = m-1
                else:
                    result[0] = m
                    break
            elif A[m] > target:
                e = m - 1
            else:
                s = m + 1
        if result[0] == -1:
            return result
        s,e = result[0], length-1
        while s <= e:
            m = s + (e-s)/2
            if A[m] == target:
                if m+1 <= e:
                    if A[m+1] != target:
                        result[1] = m
                        break
                    else:
                        s = m+1
                else:
                    result[1] = m
                    break
            elif A[m] > target:
                e = m-1
            else:
                s = m+1
        return result
A = [5, 7, 7, 8, 8, 10]
target = 10
sol = Solution()
print sol.searchRange(A, target)
