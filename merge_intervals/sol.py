# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        s1 = sorted(intervals, key=lambda x: x[0])
        return self.myMerge(intervals)
    def myMerge(self, intervals):
        while True:
            modified = False
            index = 0
            newb, newe = 0,0
            for i in range(1,len(intervals)):
                b1, e1 = intervals[i-1][0], intervals[i-1][1]
                b2, e2 = intervals[i][0], intervals[i][1]
                if b1 <= b2 and b2 <= e1:
                    newb = min(b1,b2)
                    newe = max(e1,e2)
                    modified = True
                    index = i
                    break
            if modified:
                intervals.pop(index)
                intervals.pop(index-1)
                intervals.insert(index-1, [newb, newe])
                return self.myMerge(intervals)
            else:
                return intervals
inte = [[1,3],[2,6],[8,10],[15,18]]
print inte
sol = Solution()
rst = sol.merge(inte)
print rst
