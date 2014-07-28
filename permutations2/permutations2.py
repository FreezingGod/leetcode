class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num = sorted(num)
        visited = [0] * len(num)
        result = []
        level = 1
        for per in self.mypermute(visited, num, level):
            result.append(per)
        return result
    def mypermute(self, visited, num, level):
        if level == len(num):
            for i in range(len(num)):
                if not visited[i]:
                    yield [num[i]]
        for i in range(len(num)):
            if not visited[i]:
                if (i > 0 and num[i] == num[i-1] and visited[i-1] == 0):
                    continue
                visited[i] = 1
                for per in self.mypermute(visited, num, level+1):
                    yield [num[i]] + per
                visited[i] = 0

num = [1,1,2]
sol = Solution()
print sol.permuteUnique(num)
