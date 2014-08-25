class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if not m: return 0
        n = len(matrix[0])
        if not n: return 0
        height = [[0]*n for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(n):
                if matrix[i-1][j] == "0":
                    height[i][j] = 0
                else:
                    height[i][j] = height[i-1][j]+1
        largest = 0
        print height
        for i in range(1, m+1):
            largest = max(largest, self.largest(height[i]))
        return largest
    def largest(self, height):
        height.append(0)
        stack = []
        index = []
        largest = 0
        for i in range(len(height)):
            if not stack or stack[-1] < height[i]:
                stack.append(height[i])
                index.append(i)
            else:
                top, idx = stack.pop(), index.pop()
                while True:
                    largest = max(largest, top*(i-idx))
                    if stack and stack[-1] > height[i]:
                        top = stack.pop()
                        idx = index.pop()
                    else:
                        stack.append(height[i])
                        index.append(idx)
                        break
        return largest

matrix = [[0]]
sol = Solution()
print sol.maximalRectangle(matrix)
