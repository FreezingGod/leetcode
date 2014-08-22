# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        points.sort(key=lambda x:x.x)
        largest = -1
        for i in range(len(points)):
            slop = {'inf': 1}
            samePoint = 0
            x1, y1 = points[i].x, points[i].y
            for j in range(i+1, len(points)):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2:
                    if y1 == y2:
                        samePoint += 1
                    else:
                        slop['inf'] += 1
                else:
                    s = float(y2-y1)/(x2-x1)
                    if s in slop:
                        slop[s] += 1
                    else:
                        slop[s] = 2
            largest = max(largest, max(slop.values())+samePoint)
        return largest
