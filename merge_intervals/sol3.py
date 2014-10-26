
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) <= 1: return intervals
        intervals = sorted(intervals, key = lambda x:x[0])
        result = []
        result.append(intervals[0])
        for k in range(1, len(intervals)):
            m, n = intervals[k][0], intervals[k][1]
            i, j = result[-1][0], result[-1][1]
            if m <= j:
                result[-1][0] = min(m, i)
                result[-1][1] = max(n, j)
            else:
                result.append([m,n])
        return result

sol = Solution()
print sol.merge([[1,4],[1,4]])
