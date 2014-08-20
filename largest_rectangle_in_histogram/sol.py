# O(n^2) algorithm, got TLE
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        largest = 0
        for i in range(len(height)):
            h = height[i]
            for j in range(i, len(height)):
                if height[j] < h:
                    h = height[j]
                area = h*(j-i+1)
                if area > largest:
                    largest = area
        return largest
