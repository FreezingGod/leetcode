class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        visited = [0] * len(num)
        for i in self.mypermute(num, visited, level = 1):
            result.append(i)
        return result
    def mypermute(self, num, visited, level):
        if level == len(num):
            for i in range(len(num)):
                if not visited[i]:
                    yield [num[i]]
        for i in range(len(num)):
            if not visited[i]:
                visited[i] = 1
                for per in self.mypermute(num, visited, level+1):
                    yield [num[i]] + per
                visited[i] = 0

num = [1,2,3]
sol = Solution()
print sol.permute(num)
