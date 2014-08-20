# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def p(self):
        print self.start, self.end
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        s1 = sorted(intervals, key=lambda x: x.start)
        return self.myMerge(s1)
    def myMerge(self, intervals):
        last = 1
        while True:
            modified = False
            index = 0
            newb, newe = 0,0
            for i in range(last,len(intervals)):
                b1, e1 = intervals[i-1].start, intervals[i-1].end
                b2, e2 = intervals[i].start, intervals[i].end
                if b1 <= b2 and b2 <= e1:
                    newb = min(b1,b2)
                    newe = max(e1,e2)
                    modified = True
                    index = i
                    break
            if modified:
                intervals.pop(index)
                intervals.pop(index-1)
                intervals.insert(index-1, Interval(newb,newe))
                last = index
                modified = False
                index = 0
                newb, newe = 0,0
            else:
                return intervals

lst = [[1,3],[2,6],[8,10],[15,18]]
l = [Interval(i[0],i[1]) for i in lst]
sol = Solution()
rst = sol.merge(l)
for i in rst:
    i.p()
