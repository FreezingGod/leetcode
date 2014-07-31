class Solution:
    # @return an integer
    def maxArea(self, height):
        l, r = 0, len(height)-1
        largest = 0
        while l < r:
            area = (r-l)*min(height[l],height[r])
            if area > largest:
                largest = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return largest

