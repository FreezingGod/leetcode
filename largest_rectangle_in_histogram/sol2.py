class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        h, w = [], []
        largest = 0
        height.append(0)
        for i in range(len(height)):
            if not h or h[-1] <= height[i]:
                h.append(height[i])
                w.append(i)
            else:
                idx = 0
                while h and h[-1] > height[i]:
                    ch = h.pop()
                    idx = w.pop()
                    area = ch*(i-idx)
                    if area > largest:
                        largest = area
                h.append(height[i])
                w.append(idx)
            print h, w, largest
        return largest
height = [4,2,0,3,2,5]
height = [2,1,2]
sol = Solution()
print sol.largestRectangleArea(height)
