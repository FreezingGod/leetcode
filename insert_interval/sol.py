# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        result = []
        nb, ne = newInterval.start, newInterval.end
        for i in intervals:
            b, e = i.start, i.end
            if e < nb:
                result.append(Interval(b,e))
            elif b <= nb and nb <= e or nb <= b and b <= ne:
                nb, ne = min(b, nb), max(e, ne)
            elif b > ne:
                result.append(Interval(nb, ne))
                nb, ne = b, e
        result.append(Interval(nb,ne))
        return result
l = [[1,2],[3,5],[6,7],[8,10],[12,16]]
i = [4,9]
sol = Solution()
print sol.insert(l, i)
