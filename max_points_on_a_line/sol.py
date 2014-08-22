# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points: return 0
        points, mul = self.deduplication(points)
        if len(points) == 1: return mul[0]
        slopd = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i].x, points[i].y
                x2, y2 = points[j].x, points[j].y
                if x1 == x2:
                    slopd['infinity'] = slopd.get('infinity', [])
                    slopd['infinity'].append((i,j))
                else:
                    slop = float(y2-y1)/(x2-x1)
                    slopd[slop] = slopd.get(slop, [])
                    slopd[slop].append((i,j))
        largest = 0
        for lst in sorted(slopd.values(), key = lambda x: len(x), reverse=True):
            csets = [set()]
            csets[0].add(lst[0][0]); csets[0].add(lst[0][1])
            for k in range(1, len(lst)):
                i,j = lst[k][0], lst[k][1]
                added = False
                for cset in csets:
                    if i in cset or j in cset:
                        cset.add(i); cset.add(j)
                        added = True
                        break
                if not added:
                    csets.append(set([i,j]))
            for cset in csets:
                num = sum([mul[i] for i in cset])
                if num > largest:
                    largest = num
        return largest

    def deduplication(self, points):
        if not points: return (points, [])
        multiplicity = []
        result = []
        points.sort(key = lambda x: x.x)
        last = -1
        for i in range(0, len(points)):
            if last < 0:
                result.append(points[i])
                multiplicity.append(1)
                last = 0
                continue
            lx,ly = points[last].x, points[last].y
            x, y = points[i].x, points[i].y
            if lx == x and ly == y:
                multiplicity[-1] += 1
            else:
                result.append(points[i])
                multiplicity.append(1)
                last = i
        return (result, multiplicity)
