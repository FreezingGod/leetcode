class Solution:
    # @return an integer
    def maxArea(self, height):
        leftC, rightC = [], [] # left and right candidates
        longest = 0
        for i in range(len(height)):
            if height[i] > longest:
                longest = height[i]
                leftC.append((i,height[i]))
        longest = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > longest:
                longest = height[i]
                rightC.append((i,height[i]))
        largest = 0
        for l,lh in leftC:
            for r, rh in rightC:
                if l > r:
                    break
                area = min(lh,rh)*(r-l)
                if area > largest:
                    largest = area
        return largest
